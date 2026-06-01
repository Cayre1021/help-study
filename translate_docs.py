import os
import json
import urllib.request
import urllib.parse
import urllib.error
import time
import sys

# Reconfigure stdout to use UTF-8 on Windows to prevent GBK encoding errors
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# File paths
DOCS_PATH = "raw_data/parsed_docs.json"
STRINGS_PATH = "raw_data/strings_to_translate.json"
CACHE_PATH = "raw_data/translation_cache.json"
OUTPUT_PATH = "raw_data/parsed_docs_zh.json"

# Load source files
with open(DOCS_PATH, "r", encoding="utf-8") as f:
    docs = json.load(f)

with open(STRINGS_PATH, "r", encoding="utf-8") as f:
    strings_to_translate = json.load(f)

# Load cache if it exists
translation_cache = {}
if os.path.exists(CACHE_PATH):
    try:
        with open(CACHE_PATH, "r", encoding="utf-8") as f:
            translation_cache = json.load(f)
        print(f"Loaded {len(translation_cache)} cached translations.")
    except Exception as e:
        print(f"Error loading cache: {e}")

# Filter strings that need translation
todo_strings = [s for s in strings_to_translate if s not in translation_cache]
print(f"Total strings to translate: {len(strings_to_translate)}")
print(f"Already cached: {len(translation_cache)}")
print(f"Remaining to fetch: {len(todo_strings)}")

def save_cache():
    with open(CACHE_PATH, "w", encoding="utf-8") as f:
        json.dump(translation_cache, f, indent=2, ensure_ascii=False)

def translate_single_string(text):
    stripped = text.strip()
    if not stripped or stripped.isdigit():
        return text
        
    url_text = urllib.parse.quote(text)
    # Using Google Translate single API which has high rate limits and is very stable
    url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=zh-CN&dt=t&q={url_text}"
    
    retries = 3
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=10) as response:
                res_data = json.loads(response.read().decode('utf-8'))
                
            # Parse Google single translation response
            # Format: [[[translated_text, original_text, ...], ...], ...]
            if res_data and len(res_data) > 0 and res_data[0]:
                translated_text = "".join(segment[0] for segment in res_data[0] if segment and segment[0])
                
                # Cleanup common translations
                translated_text = translated_text.replace("@ tailwindcss", "@tailwindcss")
                translated_text = translated_text.replace(" postcss", " postcss")
                translated_text = translated_text.replace("&lt; head &gt;", "&lt;head&gt;")
                translated_text = translated_text.replace("&lt;head &gt;", "&lt;head&gt;")
                translated_text = translated_text.replace("&lt; head&gt;", "&lt;head&gt;")
                translated_text = translated_text.replace("&lt; /head&gt;", "&lt;/head&gt;")
                translated_text = translated_text.replace("&lt;/ head&gt;", "&lt;/head&gt;")
                translated_text = translated_text.replace("postcss.config.js", "postcss.config.js")
                translated_text = translated_text.replace("tailwind.config.js", "tailwind.config.js")
                
                return translated_text
            else:
                print(f"Empty translation from Google on attempt {attempt+1}")
                time.sleep(1)
        except Exception as e:
            print(f"Error on attempt {attempt+1}: {str(e)[:100]}")
            time.sleep(2)
            
    print("Failed to translate via API. Falling back to original.")
    return text

# Run translations sequentially
if todo_strings:
    print("Starting sequential translations using Google API...")
    count = 0
    for idx, s in enumerate(todo_strings):
        translated = translate_single_string(s)
        translation_cache[s] = translated
        count += 1
        
        # Save cache every 5 completions
        if count % 5 == 0:
            save_cache()
            print(f"Progress: {idx+1}/{len(todo_strings)} processed...")
            
        # Tiny delay to avoid hit peaks
        time.sleep(0.2)
        
    save_cache()
    print("All translation fetches finished.")

# Ensure translation_cache has mapping for all strings
for s in strings_to_translate:
    if s not in translation_cache:
        translation_cache[s] = s

# Apply translations to copy of parsed_docs
print("Translating parsed_docs data structure...")

zh_docs = {
    "general": {},
    "frameworks": {}
}

# Translate Category 1: General
for page, pdata in docs["general"].items():
    zh_docs["general"][page] = {
        "title": translation_cache.get(pdata["title"], pdata["title"]),
        "description": translation_cache.get(pdata["description"], pdata["description"]),
        "tile": None,
        "steps": []
    }
    for step in pdata["steps"]:
        zh_docs["general"][page]["steps"].append({
            "title": translation_cache.get(step["title"], step["title"]),
            "body": translation_cache.get(step["body"], step["body"]),
            "code": step["code"]
        })

# Translate Category 2: Frameworks
for page, pdata in docs["frameworks"].items():
    tile_data = None
    if pdata.get("tile"):
        tile_data = {
            "title": translation_cache.get(pdata["tile"]["title"], pdata["tile"]["title"]),
            "description": translation_cache.get(pdata["tile"]["description"], pdata["tile"]["description"])
        }
        
    zh_docs["frameworks"][page] = {
        "title": translation_cache.get(pdata["title"], pdata["title"]),
        "description": translation_cache.get(pdata["description"], pdata["description"]),
        "tile": tile_data,
        "steps": []
    }
    for step in pdata["steps"]:
        zh_docs["frameworks"][page]["steps"].append({
            "title": translation_cache.get(step["title"], step["title"]),
            "body": translation_cache.get(step["body"], step["body"]),
            "code": step["code"]
        })

# Save translated JSON
with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    json.dump(zh_docs, f, indent=2, ensure_ascii=False)

print(f"Translation completed. Output saved to {OUTPUT_PATH}")
