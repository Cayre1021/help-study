import os
import re
import json
import urllib.request
import urllib.error

# Setup raw directories
os.makedirs("raw_data/tabs", exist_ok=True)
os.makedirs("raw_data/frameworks", exist_ok=True)

base_raw_url = "https://raw.githubusercontent.com/tailwindlabs/tailwindcss.com/main"

general_pages = ["using-vite", "using-postcss", "tailwind-cli", "play-cdn"]
framework_pages = [
    "nextjs", "laravel", "nuxtjs", "solidjs", "sveltekit", "gatsby", 
    "angular", "ruby-on-rails", "react-router", "tanstack-start", 
    "phoenix", "parcel", "symfony", "meteor", "adonisjs", "emberjs", 
    "astro", "qwik", "rspack"
]

def download_file(url, dest):
    if os.path.exists(dest):
        return True
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            content = response.read()
        with open(dest, "wb") as f:
            f.write(content)
        return True
    except urllib.error.HTTPError as e:
        print(f"Error downloading {url}: {e.code}")
        return False
    except Exception as e:
        print(f"Error downloading {url}: {str(e)}")
        return False

# Download files if missing
print("Downloading missing source files from GitHub...")
for page in general_pages:
    url = f"{base_raw_url}/src/app/(docs)/docs/installation/(tabs)/{page}/page.tsx"
    download_file(url, f"raw_data/tabs/{page}.tsx")

for page in framework_pages:
    url = f"{base_raw_url}/src/app/(docs)/docs/installation/framework-guides/{page}.tsx"
    download_file(url, f"raw_data/frameworks/{page}.tsx")

def clean_jsx_body(body_str):
    body_str = body_str.strip()
    if body_str.startswith('(') and body_str.endswith(')'):
        body_str = body_str[1:-1].strip()
    
    # Clean JSX braces
    body_str = re.sub(r'\{\s*" "\s*\}', ' ', body_str)
    body_str = re.sub(r'\{\s*"([^"]*)"\s*\}', r'\1', body_str)
    body_str = re.sub(r"\{\s*'([^']*)'\s*\}", r'\1', body_str)
    body_str = re.sub(r'\{\s*([^}]*)\s*\}', r'\1', body_str)
    
    # Normalize directional smart quotes
    body_str = body_str.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    
    # Clean whitespace
    body_str = re.sub(r'\s+', ' ', body_str)
    body_str = body_str.replace('> <', '><').strip()
    return body_str

def extract_nested_braces(text, start_pos):
    brace_count = 0
    in_backtick = False
    escaped = False
    
    i = start_pos
    while i < len(text):
        char = text[i]
        if escaped:
            escaped = False
            i += 1
            continue
        if char == '\\':
            escaped = True
            i += 1
            continue
        if char == '`':
            in_backtick = not in_backtick
            i += 1
            continue
        if not in_backtick:
            if char == '{':
                brace_count += 1
            elif char == '}':
                brace_count -= 1
                if brace_count == 0:
                    return text[start_pos:i+1], i
        i += 1
    return None, -1

def parse_tsx_file(filepath, is_framework=False):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    page_title = ""
    page_description = ""
    tile_title = ""
    tile_description = ""
    
    # 1. Parse page title and description
    metadata_match = re.search(r'(?:const|let|export let|export const)\s+(?:metadata|page)\s*(?::\s*\w+)?\s*=\s*(\{.*?\})', content, re.DOTALL)
    if metadata_match:
        obj_text = metadata_match.group(1)
        t_match = re.search(r'title:\s*(?:"([^"]*)"|\'([^\']*)\'|`([^`]*)`)', obj_text)
        if t_match:
            page_title = next(g for g in t_match.groups() if g is not None)
        d_match = re.search(r'description:\s*(?:"([^"]*)"|\'([^\']*)\'|`([^`]*)`)', obj_text, re.DOTALL)
        if d_match:
            page_description = next(g for g in d_match.groups() if g is not None)
            page_description = re.sub(r'\s+', ' ', page_description).strip()
            
    # Fallbacks
    if not page_title:
        t_match = re.search(r'export let page\s*(?::\s*\w+)?\s*=\s*\{\s*title:\s*(?:"([^"]*)"|\'([^\']*)\')', content)
        if t_match:
            page_title = next(g for g in t_match.groups() if g is not None)
        else:
            # Fallback to general title
            t_match = re.search(r'title:\s*(?:"([^"]*)"|\'([^\']*)\')', content)
            if t_match:
                page_title = next(g for g in t_match.groups() if g is not None)

    # 2. Parse tile metadata (for frameworks grid)
    tile_match = re.search(r'export let tile\s*(?::\s*\w+)?\s*=\s*(\{.*?\})', content, re.DOTALL)
    if tile_match:
        tile_obj = tile_match.group(1)
        t_match = re.search(r'title:\s*(?:"([^"]*)"|\'([^\']*)\')', tile_obj)
        if t_match:
            tile_title = next(g for g in t_match.groups() if g is not None)
        d_match = re.search(r'description:\s*(?:"([^"]*)"|\'([^\']*)\')', tile_obj)
        if d_match:
            tile_description = next(g for g in d_match.groups() if g is not None)
            
    if not page_title and tile_title:
        page_title = f"Install Tailwind CSS with {tile_title}"
    if not page_description and tile_description:
        page_description = f"Setting up Tailwind CSS in a {tile_title} project."

    # 3. Extract steps array
    steps = []
    steps_decl = re.search(r'(?:const|let|export let)\s+steps\s*(?::\s*\w+\[\])?\s*=\s*\[', content)
    if steps_decl:
        start_idx = steps_decl.end() - 1
        
        bracket_count = 1
        in_backtick = False
        escaped = False
        i = start_idx + 1
        steps_text = ""
        while i < len(content):
            char = content[i]
            if escaped:
                escaped = False
                i += 1
                continue
            if char == '\\':
                escaped = True
                i += 1
                continue
            if char == '`':
                in_backtick = not in_backtick
                i += 1
                continue
            if not in_backtick:
                if char == '[':
                    bracket_count += 1
                elif char == ']':
                    bracket_count -= 1
                    if bracket_count == 0:
                        steps_text = content[start_idx:i+1]
                        break
            i += 1
            
        pos = 0
        while True:
            next_brace = steps_text.find('{', pos)
            if next_brace == -1:
                break
            
            step_obj, end_pos = extract_nested_braces(steps_text, next_brace)
            if not step_obj:
                break
                
            t_match = re.search(r'title:\s*(?:"([^"]*)"|\'([^\']*)\')', step_obj)
            if t_match:
                step_title = next(g for g in t_match.groups() if g is not None)
            else:
                step_title = "Step"
                
            body_match = re.search(r'body:\s*(.*?),\s*(?:code|href|logo|tile):', step_obj, re.DOTALL)
            if body_match:
                step_body = clean_jsx_body(body_match.group(1))
            else:
                body_match = re.search(r'body:\s*(.*?)\s*\}', step_obj, re.DOTALL)
                step_body = clean_jsx_body(body_match.group(1)) if body_match else ""
                
            code_name = ""
            code_lang = ""
            code_val = ""
            
            code_start_idx = step_obj.find('code: {')
            if code_start_idx != -1:
                code_obj_start = code_start_idx + len('code: ')
                code_obj, _ = extract_nested_braces(step_obj, code_obj_start)
                if code_obj:
                    n_match = re.search(r'name:\s*(?:"([^"]*)"|\'([^\']*)\')', code_obj)
                    if n_match:
                        code_name = next(g for g in n_match.groups() if g is not None)
                    l_match = re.search(r'lang:\s*(?:"([^"]*)"|\'([^\']*)\')', code_obj)
                    if l_match:
                        code_lang = next(g for g in l_match.groups() if g is not None)
                    v_match = re.search(r'code:\s*(?:dedent|shell|js|css|html|config)?`([\s\S]*?)`', code_obj)
                    if v_match:
                        code_val = v_match.group(1).strip()
                        # Normalize directional smart quotes in code blocks
                        code_val = code_val.replace("’", "'").replace("‘", "'")
                    
            steps.append({
                "title": step_title,
                "body": step_body,
                "code": {
                    "name": code_name,
                    "lang": code_lang,
                    "code": code_val
                }
            })
            pos = end_pos + 1
            
    return {
        "title": page_title,
        "description": page_description,
        "tile": {
            "title": tile_title,
            "description": tile_description
        } if tile_title else None,
        "steps": steps
    }

print("Parsing files...")
all_data = {
    "general": {},
    "frameworks": {}
}

for page in general_pages:
    filepath = f"raw_data/tabs/{page}.tsx"
    print(f"Parsing {filepath}...")
    all_data["general"][page] = parse_tsx_file(filepath, is_framework=False)

for page in framework_pages:
    filepath = f"raw_data/frameworks/{page}.tsx"
    print(f"Parsing {filepath}...")
    all_data["frameworks"][page] = parse_tsx_file(filepath, is_framework=True)

# Save parsed data to JSON
with open("raw_data/parsed_docs.json", "w", encoding="utf-8") as f:
    json.dump(all_data, f, indent=2, ensure_ascii=False)

print("Scraping and parsing completed. Data saved to raw_data/parsed_docs.json.")
