import os
import json
import re

# Ensure folders exist
os.makedirs("assets", exist_ok=True)

# Load parsed JSON
with open("raw_data/parsed_docs_zh.json", "r", encoding="utf-8") as f:
    docs = json.load(f)

# Framework icon mapping (SVG paths and colors)
# We will define inline SVGs for frameworks to make it look premium
svg_icons = {
    "nextjs": '<svg width="32" height="32" class="w-8 h-8" viewBox="0 0 180 180" fill="currentColor"><path d="M145.47 160.28c-1.3-.9-2.73-1.63-4.14-2.48l-68.51-87.97V139.3h-12.63V52.88h11.23l66.97 86.42V52.88h12.63v107.4a33.56 33.56 0 0 1-5.55 0Zm-55.47 9.72c-49.63 0-90-40.37-90-90s40.37-90 90-90 90 40.37 90 90c0 19.34-6.11 37.26-16.53 51.98l-10.4-13.38A77.06 77.06 0 0 0 167.37 90c0-42.66-34.71-77.37-77.37-77.37S12.63 47.34 12.63 90s34.71 77.37 77.37 77.37c15.22 0 29.35-4.4 41.34-11.96l10.41 13.38A89.65 89.65 0 0 1 90 170Z"/></svg>',
    "laravel": '<svg width="32" height="32" class="w-8 h-8 text-red-600" viewBox="0 0 24 24" fill="currentColor"><path d="M20.354 4.542l-5.698-3.284a1.365 1.365 0 0 0-1.363 0l-5.699 3.284a1.365 1.365 0 0 0-.682 1.182v6.57l-1.342.775V6.505c0-.493-.264-.95-.694-1.198L3.218 4.303a1.397 1.397 0 0 0-1.398 0c-.43.248-.694.705-.694 1.198v9.988c0 .493.264.95.694 1.198l5.658 3.262a1.397 1.397 0 0 0 1.398 0l5.658-3.262c.43-.248.694-.705.694-1.198v-6.57l1.342-.775v6.565c0 .493.264.95.694 1.198l1.658.958a1.397 1.397 0 0 0 1.398 0l5.658-3.262c.43-.248.694-.705.694-1.198V5.724a1.365 1.365 0 0 0-.682-1.182zM4.17 14.887V7.121l4.288 2.472v7.766L4.17 14.887zm11.233-1.63V5.491l4.288 2.472v7.766L15.403 13.257z"/></svg>',
    "nuxtjs": '<svg width="32" height="32" class="w-8 h-8 text-emerald-500" viewBox="0 0 24 24" fill="currentColor"><path d="M22.5 19.5h-21l10.5-16.5 10.5 16.5zm-15.545-2.25h10.09L12 9.409 6.955 17.25zM12 11.25l1.682 2.62h-3.364L12 11.25z"/></svg>',
    "solidjs": '<svg width="32" height="32" class="w-8 h-8 text-sky-500" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2A10 10 0 0 0 2 12a10 10 0 0 0 10 10 10 10 0 0 0 10-10A10 10 0 0 0 12 2zm3.89 12.3L12.3 17.89a.43.43 0 0 1-.6 0L8.11 14.3a.43.43 0 0 1 0-.6l3.59-3.59a.43.43 0 0 1 .6 0l3.59 3.59c.17.17.17.44 0 .6z"/></svg>',
    "sveltekit": '<svg width="32" height="32" class="w-8 h-8 text-orange-500" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm4.85 14.15c-.2.2-.51.2-.71 0l-3.29-3.29V8.5a.5.5 0 0 0-1 0v4.71l-1.65-1.65a.5.5 0 0 0-.71.71l2 2c.2.2.51.2.71 0l4-4a.5.5 0 0 0-.71-.71l-3.64 3.64z"/></svg>',
    "gatsby": '<svg width="32" height="32" class="w-8 h-8 text-purple-600" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8 0-1.89.66-3.63 1.77-5.02l11.25 11.25c-1.39 1.11-3.13 1.77-5.02 1.77zm6.23-2.98L7.02 5.77C8.41 4.66 10.15 4 12 4c4.41 0 8 3.59 8 8 0 1.89-.66 3.63-1.77 5.02z"/></svg>',
    "angular": '<svg width="32" height="32" class="w-8 h-8 text-red-500" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2L2 5.5l1.5 13.5L12 22l8.5-3L22 5.5zM12 4.6l6.8 2.4-1.1 9.4L12 18.8l-5.7-2.4-1.1-9.4zM12 6.5L7.7 15.5h2.1l1-2.4h2.4l1 2.4h2.1zm-1.1 5.3l1.1-2.6 1.1 2.6z"/></svg>',
    "ruby-on-rails": '<svg width="32" height="32" class="w-8 h-8 text-red-700" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 14.5h-2v-4H9v-2h2v-2h2v2h2v2h-2z"/></svg>',
    "react-router": '<svg width="32" height="32" class="w-8 h-8" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-2h2v2zm1.07-7.75l-.9.92C12.45 10.9 12 11.5 12 13h-2v-.5c0-1.1.45-2.1 1.17-2.83l1.24-1.26c.37-.36.59-.86.59-1.41 0-1.1-.9-2-2-2s-2 .9-2 2H7c0-2.76 2.24-5 5-5s5 2.24 5 5c0 1.04-.42 1.99-1.07 2.75z"/></svg>',
    "tanstack-start": '<svg width="32" height="32" class="w-8 h-8 text-teal-500" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8h3v-2H4c0-4.41 3.59-8 8-8s8 3.59 8 8h-3v2h3c0 4.41-3.59 8-8 8z"/></svg>',
    "phoenix": '<svg width="32" height="32" class="w-8 h-8 text-orange-600" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2L2 7l10 5 10-5zm0 10.5L3.5 8v6.5l8.5 4.5 8.5-4.5V8z"/></svg>',
    "parcel": '<svg width="32" height="32" class="w-8 h-8 text-amber-700" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.2L2.5 7.7v8.6l9.5 5.5 9.5-5.5V7.7zm0 2.4l7.1 4.1-7.1 4.1-7.1-4.1zM4.5 9.6l6.5 3.8v6.7l-6.5-3.8zm15 3.8l-6.5 3.8v-6.7l6.5-3.8z"/></svg>',
    "symfony": '<svg width="32" height="32" class="w-8 h-8 text-black dark:text-white" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm2.93 13.07a4.04 4.04 0 0 1-5.86 0 4.2 4.2 0 0 1 0-5.86 4.04 4.04 0 0 1 5.86 0c.39.4.58.9.58 1.43s-.2 1.03-.58 1.43z"/></svg>',
    "meteor": '<svg width="32" height="32" class="w-8 h-8 text-orange-500" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2A10 10 0 0 0 2 12a10 10 0 0 0 10 10 10 10 0 0 0 10-10A10 10 0 0 0 12 2zm1.25 15h-2.5v-2h2.5zm1.5-3.5h-5.5V11h5.5z"/></svg>',
    "adonisjs": '<svg width="32" height="32" class="w-8 h-8 text-indigo-600" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2L2 7l10 5 10-5zm-1 15.5l-6.5-3.5V9l6.5 3.5zm2 0V12.5l6.5-3.5v5z"/></svg>',
    "emberjs": '<svg width="32" height="32" class="w-8 h-8 text-rose-500" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm3.89 14.3L12.3 17.89a.43.43 0 0 1-.6 0L8.11 14.3a.43.43 0 0 1 0-.6l3.59-3.59a.43.43 0 0 1 .6 0l3.59 3.59c.17.17.17.44 0 .6z"/></svg>',
    "astro": '<svg width="32" height="32" class="w-8 h-8 text-rose-500" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2L2 12l10 10 10-10L12 2zm0 3.8l6.2 6.2-6.2 6.2L5.8 12 12 5.8z"/></svg>',
    "qwik": '<svg width="32" height="32" class="w-8 h-8 text-sky-500" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8 0-1.89.66-3.63 1.77-5.02L17.02 17C15.63 18.11 13.89 18.8 12 18.8z"/></svg>',
    "rspack": '<svg width="32" height="32" class="w-8 h-8 text-sky-400" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1.5 14v-4H8v-2h2.5V7.5h2v2.5H15v2h-2.5V16h-2z"/></svg>',
    
    # Tabs icons
    "tailwind-cli": '<svg width="24" height="24" class="w-6 h-6 text-sky-400" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M8 9l3 3-3 3m5 0h3M5 20h14a2 2 0 002-2V6a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>',
    "using-postcss": '<svg width="24" height="24" class="w-6 h-6 text-orange-500" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z"/></svg>',
    "using-vite": '<svg width="24" height="24" class="w-6 h-6 text-yellow-500" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M13 10V3L4 14h7v7l9-11h-7z"/></svg>',
    "play-cdn": '<svg width="24" height="24" class="w-6 h-6 text-pink-500" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z"/><path stroke-linecap="round" stroke-linejoin="round" d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>',
    "framework-guides": '<svg width="24" height="24" class="w-6 h-6 text-indigo-500" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"/></svg>'
}

def get_icon(key):
    return svg_icons.get(key, '<svg width="32" height="32" class="w-8 h-8" fill="currentColor" viewBox="0 0 24 24"><rect width="20" height="20" x="2" y="2" rx="4"/></svg>')

# ----------------- Step Code Tab Switching Translator -----------------
def translate_command(cmd, target_pm):
    lines = cmd.split('\n')
    translated = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            translated.append(line)
            continue
        
        indent = line[:len(line) - len(line.lstrip())]
        
        # 1. npm create
        if stripped.startswith('npm create '):
            parts = stripped.split(' ')
            pkg = parts[2].split('@')[0]
            rest = ' '.join(parts[3:])
            if target_pm == 'npm':
                line_trans = stripped
            elif target_pm == 'yarn':
                line_trans = f"yarn create {pkg} {rest}"
            elif target_pm == 'pnpm':
                line_trans = f"pnpm create {pkg} {rest}"
            elif target_pm == 'bun':
                line_trans = f"bun create {pkg} {rest}"
        # 2. npm install (with packages)
        elif stripped.startswith('npm install ') and len(stripped.split(' ')) > 2:
            pkgs = stripped[len('npm install '):]
            if target_pm == 'npm':
                line_trans = stripped
            elif target_pm == 'yarn':
                line_trans = f"yarn add {pkgs}"
            elif target_pm == 'pnpm':
                line_trans = f"pnpm add {pkgs}"
            elif target_pm == 'bun':
                line_trans = f"bun add {pkgs}"
        # 3. npm install (bare)
        elif stripped == 'npm install':
            if target_pm == 'npm':
                line_trans = 'npm install'
            elif target_pm == 'yarn':
                line_trans = 'yarn install'
            elif target_pm == 'pnpm':
                line_trans = 'pnpm install'
            elif target_pm == 'bun':
                line_trans = 'bun install'
        # 4. npm run
        elif stripped.startswith('npm run '):
            script = stripped[len('npm run '):]
            if target_pm == 'npm':
                line_trans = stripped
            elif target_pm == 'yarn':
                line_trans = f"yarn {script}"
            elif target_pm == 'pnpm':
                line_trans = f"pnpm {script}"
            elif target_pm == 'bun':
                line_trans = f"bun {script}"
        # 5. npx create-next-app
        elif stripped.startswith('npx create-next-app'):
            rest = stripped[len('npx create-next-app'):]
            if target_pm == 'npm':
                line_trans = stripped
            elif target_pm == 'yarn':
                line_trans = f"yarn create next-app{rest}"
            elif target_pm == 'pnpm':
                line_trans = f"pnpm create next-app{rest}"
            elif target_pm == 'bun':
                line_trans = f"bun create next-app{rest}"
        # 6. npx create-react-router
        elif stripped.startswith('npx create-react-router'):
            rest = stripped[len('npx create-react-router'):]
            if target_pm == 'npm':
                line_trans = stripped
            elif target_pm == 'yarn':
                line_trans = f"yarn create react-router{rest}"
            elif target_pm == 'pnpm':
                line_trans = f"pnpm create react-router{rest}"
            elif target_pm == 'bun':
                line_trans = f"bun create react-router{rest}"
        # 7. npx create-tanstack-start
        elif stripped.startswith('npx create-tanstack-start'):
            rest = stripped[len('npx create-tanstack-start'):]
            if target_pm == 'npm':
                line_trans = stripped
            elif target_pm == 'yarn':
                line_trans = f"yarn create tanstack-start{rest}"
            elif target_pm == 'pnpm':
                line_trans = f"pnpm create tanstack-start{rest}"
            elif target_pm == 'bun':
                line_trans = f"bun create tanstack-start{rest}"
        # 8. npx create-meteor-app
        elif stripped.startswith('npx create-meteor-app'):
            rest = stripped[len('npx create-meteor-app'):]
            if target_pm == 'npm':
                line_trans = stripped
            elif target_pm == 'yarn':
                line_trans = f"yarn create meteor-app{rest}"
            elif target_pm == 'pnpm':
                line_trans = f"pnpm create meteor-app{rest}"
            elif target_pm == 'bun':
                line_trans = f"bun create meteor-app{rest}"
        # 9. npm init adonisjs
        elif stripped.startswith('npm init adonisjs'):
            rest = stripped[len('npm init adonisjs'):]
            if target_pm == 'npm':
                line_trans = stripped
            elif target_pm == 'yarn':
                line_trans = f"yarn create adonisjs{rest}"
            elif target_pm == 'pnpm':
                line_trans = f"pnpm create adonisjs{rest}"
            elif target_pm == 'bun':
                line_trans = f"bun create adonisjs{rest}"
        # 10. npx ember-cli
        elif stripped.startswith('npx ember-cli'):
            cmd_args = stripped[len('npx ember-cli '):]
            if target_pm == 'npm':
                line_trans = stripped
            elif target_pm == 'yarn':
                line_trans = f"yarn dlx ember-cli {cmd_args}"
            elif target_pm == 'pnpm':
                line_trans = f"pnpm dlx ember-cli {cmd_args}"
            elif target_pm == 'bun':
                line_trans = f"bunx ember-cli {cmd_args}"
        # 11. npm create astro
        elif stripped.startswith('npm create astro'):
            rest = stripped[len('npm create astro'):]
            if target_pm == 'npm':
                line_trans = stripped
            elif target_pm == 'yarn':
                line_trans = f"yarn create astro{rest}"
            elif target_pm == 'pnpm':
                line_trans = f"pnpm create astro{rest}"
            elif target_pm == 'bun':
                line_trans = f"bun create astro{rest}"
        # 12. npm create qwik
        elif stripped.startswith('npm create qwik'):
            rest = stripped[len('npm create qwik'):]
            if target_pm == 'npm':
                line_trans = stripped
            elif target_pm == 'yarn':
                line_trans = f"yarn create qwik{rest}"
            elif target_pm == 'pnpm':
                line_trans = f"pnpm create qwik{rest}"
            elif target_pm == 'bun':
                line_trans = f"bun create qwik{rest}"
        # 13. npm create rsbuild / rspack
        elif stripped.startswith('npm create rsbuild') or stripped.startswith('npm create rspack'):
            rest = stripped[len('npm create '):]
            if target_pm == 'npm':
                line_trans = stripped
            elif target_pm == 'yarn':
                line_trans = f"yarn create {rest}"
            elif target_pm == 'pnpm':
                line_trans = f"pnpm create {rest}"
            elif target_pm == 'bun':
                line_trans = f"bun create {rest}"
        # 14. Generic npx command (e.g. npx sv, npx nuxi, npx @angular/cli, npx parcel, npx ember)
        elif stripped.startswith('npx '):
            cmd_args = stripped[len('npx '):]
            if target_pm == 'npm':
                line_trans = stripped
            elif target_pm == 'yarn':
                line_trans = f"yarn dlx {cmd_args}"
            elif target_pm == 'pnpm':
                line_trans = f"pnpm dlx {cmd_args}"
            elif target_pm == 'bun':
                line_trans = f"bunx {cmd_args}"
        else:
            line_trans = stripped
            
        translated.append(indent + line_trans)
        
    return '\n'.join(translated)

# ----------------- Write index.css -----------------
css_content = """/* CSS Variables for Premium Dark/Light Modes */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

:root {
  --font-sans: 'Inter', system-ui, -apple-system, sans-serif;
  --font-mono: 'JetBrains+Mono', monospace;
  
  /* Light Mode Colors */
  --bg-primary: #ffffff;
  --bg-secondary: #f8fafc;
  --bg-tertiary: #f1f5f9;
  --text-primary: #0f172a;
  --text-secondary: #475569;
  --text-muted: #94a3b8;
  --border-color: #e2e8f0;
  
  --brand-color: #0ea5e9;
  --brand-light: #e0f2fe;
  --brand-dark: #0369a1;
  
  --sidebar-active-bg: #f0f9ff;
  --sidebar-active-text: #0284c7;
  
  --code-bg: #0f172a;
  --code-text: #f8fafc;
  --code-header-bg: #1e293b;
  --code-highlight-bg: rgba(56, 189, 248, 0.1);
  --code-highlight-border: #38bdf8;
}

html.dark {
  /* Dark Mode Colors */
  --bg-primary: #0b0f19;
  --bg-secondary: #111827;
  --bg-tertiary: #1f2937;
  --text-primary: #f8fafc;
  --text-secondary: #94a3b8;
  --text-muted: #64748b;
  --border-color: #1e293b;
  
  --brand-color: #38bdf8;
  --brand-light: #075985;
  --brand-dark: #0ea5e9;
  
  --sidebar-active-bg: #07598533;
  --sidebar-active-text: #38bdf8;
  
  --code-bg: #030712;
  --code-text: #f9fafb;
  --code-header-bg: #111827;
  --code-highlight-bg: rgba(56, 189, 248, 0.08);
  --code-highlight-border: #0ea5e9;
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  transition: background-color 0.2s, border-color 0.2s;
}

body {
  font-family: var(--font-sans);
  background-color: var(--bg-primary);
  color: var(--text-primary);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  overflow-x: hidden;
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
}

/* Header bar styles */
header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: 60px;
  background-color: rgba(255, 255, 255, 0.8);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--border-color);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 24px;
  z-index: 50;
}

html.dark header {
  background-color: rgba(11, 15, 25, 0.8);
}

.header-left {
  display: flex;
  align-items: center;
  gap: 16px;
}

.logo-link {
  display: flex;
  align-items: center;
  gap: 8px;
  text-decoration: none;
  color: var(--text-primary);
  font-weight: 700;
  font-size: 1.2rem;
}

.logo-svg {
  height: 24px;
  color: #38bdf8;
}

.version-badge {
  font-size: 0.75rem;
  font-weight: 600;
  background-color: var(--bg-tertiary);
  color: var(--text-secondary);
  padding: 2px 8px;
  border-radius: 9999px;
  border: 1px solid var(--border-color);
}

.header-right {
  display: flex;
  align-items: center;
  gap: 16px;
}

.header-nav {
  display: flex;
  gap: 20px;
}

.header-nav a {
  font-size: 0.875rem;
  font-weight: 500;
  color: var(--text-secondary);
  text-decoration: none;
}

.header-nav a:hover {
  color: var(--text-primary);
}

.icon-btn {
  background: none;
  border: none;
  color: var(--text-secondary);
  cursor: pointer;
  padding: 6px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.icon-btn:hover {
  background-color: var(--bg-tertiary);
  color: var(--text-primary);
}

/* Sidebar & Main layouts */
.main-wrapper {
  display: flex;
  flex: 1;
  padding-top: 60px;
}

.sidebar-aside {
  width: 280px;
  position: fixed;
  top: 60px;
  bottom: 0;
  left: 0;
  border-right: 1px solid var(--border-color);
  background-color: var(--bg-primary);
  overflow-y: auto;
  padding: 24px;
  z-index: 40;
}

.sidebar-nav-section {
  margin-bottom: 24px;
}

.sidebar-nav-section h3 {
  font-size: 0.75rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--text-muted);
  margin-bottom: 12px;
}

.sidebar-nav-list {
  list-style: none;
}

.sidebar-nav-item a {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 8px 12px;
  font-size: 0.875rem;
  font-weight: 500;
  color: var(--text-secondary);
  text-decoration: none;
  border-radius: 8px;
  margin-bottom: 4px;
  transition: all 0.15s;
}

.sidebar-nav-item a:hover {
  background-color: var(--bg-secondary);
  color: var(--text-primary);
}

.sidebar-nav-item.active a {
  background-color: var(--sidebar-active-bg);
  color: var(--sidebar-active-text);
  font-weight: 600;
}

/* Page content area */
.content-main {
  flex: 1;
  margin-left: 280px;
  padding: 40px 48px;
  max-width: 1012px;
}

/* Stepper connection line and layouts */
.page-title {
  font-size: 2.25rem;
  font-weight: 800;
  letter-spacing: -0.025em;
  margin-bottom: 8px;
}

.page-description {
  font-size: 1.125rem;
  color: var(--text-secondary);
  margin-bottom: 32px;
  line-height: 1.6;
}

.steps-list {
  display: flex;
  flex-direction: column;
  position: relative;
  padding-left: 56px;
  margin-top: 16px;
}

.steps-list::before {
  content: '';
  position: absolute;
  left: 20px;
  top: 12px;
  bottom: 24px;
  width: 2px;
  background-color: var(--border-color);
}

.step-item {
  position: relative;
  margin-bottom: 48px;
}

.step-item:last-child {
  margin-bottom: 16px;
}

.step-number {
  position: absolute;
  left: -56px;
  top: 0;
  width: 42px;
  height: 42px;
  border-radius: 50%;
  background-color: var(--bg-primary);
  border: 2px solid var(--border-color);
  color: var(--text-secondary);
  font-size: 0.95rem;
  font-weight: 700;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
}

.step-item:hover .step-number {
  border-color: var(--brand-color);
  color: var(--brand-color);
}

.step-header {
  margin-bottom: 12px;
}

.step-title {
  font-size: 1.125rem;
  font-weight: 700;
  color: var(--text-primary);
}

.step-body {
  font-size: 0.95rem;
  line-height: 1.6;
  color: var(--text-secondary);
  margin-bottom: 16px;
}

.step-body code {
  font-family: var(--font-mono);
  background-color: var(--bg-tertiary);
  color: var(--brand-dark);
  padding: 2px 6px;
  border-radius: 6px;
  font-size: 0.85em;
  border: 1px solid var(--border-color);
}

html.dark .step-body code {
  color: var(--brand-color);
}

.step-body a {
  color: var(--brand-color);
  text-decoration: none;
  font-weight: 500;
  border-bottom: 1px dashed var(--brand-color);
}

.step-body a:hover {
  border-bottom-style: solid;
}

/* Package Manager Switched Code Blocks */
.code-container {
  border-radius: 12px;
  overflow: hidden;
  background-color: var(--code-bg);
  box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -4px rgba(0, 0, 0, 0.1);
  border: 1px solid var(--border-color);
  margin-bottom: 12px;
}

.code-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background-color: var(--code-header-bg);
  padding: 8px 16px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.05);
  font-family: var(--font-sans);
}

.code-title {
  font-size: 0.75rem;
  font-weight: 600;
  color: var(--text-muted);
}

.code-tabs {
  display: flex;
  gap: 4px;
}

.code-tab-btn {
  background: none;
  border: none;
  color: var(--text-muted);
  font-family: var(--font-sans);
  font-size: 0.75rem;
  font-weight: 600;
  padding: 4px 8px;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.15s;
}

.code-tab-btn:hover {
  color: var(--code-text);
  background-color: rgba(255, 255, 255, 0.05);
}

.code-tab-btn.active {
  color: #38bdf8;
  background-color: rgba(56, 189, 248, 0.1);
}

.code-body {
  position: relative;
  padding: 20px;
  overflow-x: auto;
}

.code-body pre {
  font-family: var(--font-mono);
  font-size: 0.875rem;
  line-height: 1.7;
  color: var(--code-text);
  margin: 0;
  white-space: pre;
}

/* Highlights in code */
.highlight-line {
  display: block;
  background-color: var(--code-highlight-bg);
  border-left: 2px solid var(--code-highlight-border);
  margin: 0 -20px;
  padding: 0 18px;
}

/* Copy button */
.copy-btn {
  background: none;
  border: none;
  color: var(--text-muted);
  cursor: pointer;
  padding: 4px;
  border-radius: 6px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.15s;
}

.copy-btn:hover {
  color: var(--code-text);
  background-color: rgba(255, 255, 255, 0.05);
}

/* Toggle displays for package managers client-side */
body.pm-npm .code-block-pnpm, body.pm-npm .code-block-yarn, body.pm-npm .code-block-bun { display: none; }
body.pm-yarn .code-block-npm, body.pm-yarn .code-block-pnpm, body.pm-yarn .code-block-bun { display: none; }
body.pm-pnpm .code-block-npm, body.pm-pnpm .code-block-yarn, body.pm-pnpm .code-block-bun { display: none; }
body.pm-bun .code-block-npm, body.pm-bun .code-block-yarn, body.pm-bun .code-block-pnpm { display: none; }

/* Grid of Cards on framework-guides.html */
.frameworks-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
  gap: 20px;
  margin-top: 24px;
}

.framework-card {
  display: flex;
  flex-direction: column;
  padding: 24px;
  background-color: var(--bg-secondary);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  text-decoration: none;
  color: var(--text-primary);
  transition: all 0.2s;
  box-shadow: 0 4px 6px -1px rgba(0,0,0,0.02);
}

.framework-card:hover {
  transform: translateY(-4px);
  border-color: var(--brand-color);
  box-shadow: 0 10px 15px -3px rgba(0,0,0,0.05), 0 4px 6px -4px rgba(0,0,0,0.05);
}

.framework-card-header {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 12px;
}

.framework-card-title {
  font-size: 1.1rem;
  font-weight: 700;
}

.framework-card-desc {
  font-size: 0.85rem;
  color: var(--text-secondary);
  line-height: 1.5;
}

/* Mobile responsive navigation styles */
.menu-toggle {
  display: none;
}

.sidebar-backdrop {
  display: none;
  position: fixed;
  top: 60px;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.4);
  backdrop-filter: blur(4px);
  -webkit-backdrop-filter: blur(4px);
  z-index: 35;
  transition: opacity 0.25s ease-in-out;
}

.sidebar-backdrop.open {
  display: block;
}

@media (max-width: 900px) {
  .sidebar-aside {
    transform: translateX(-100%);
    transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.1);
  }
  
  html.dark .sidebar-aside {
    box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.5), 0 8px 10px -6px rgba(0, 0, 0, 0.5);
  }
  
  .sidebar-aside.open {
    transform: translateX(0);
  }
  
  .content-main {
    margin-left: 0;
    padding: 30px 20px;
  }
  
  .menu-toggle {
    display: flex;
  }
  
  .header-nav {
    display: none;
  }
}

/* Extra mobile refinements for very small screens */
@media (max-width: 640px) {
  header {
    padding: 0 16px;
  }
  
  .version-badge {
    display: none; /* Hide version badge on very small screens to make room for logo */
  }
  
  .page-title {
    font-size: 1.75rem;
    letter-spacing: -0.02em;
  }
  
  .page-description {
    font-size: 0.95rem;
    margin-bottom: 24px;
  }
  
  .content-main {
    padding: 24px 16px;
  }
  
  .steps-list {
    padding-left: 44px;
  }
  
  .steps-list::before {
    left: 14px;
    top: 10px;
  }
  
  .step-number {
    left: -44px;
    width: 30px;
    height: 30px;
    font-size: 0.8rem;
  }
  
  .step-title {
    font-size: 1rem;
  }
  
  .step-body {
    font-size: 0.875rem;
  }
  
  .code-body {
    padding: 14px;
  }
  
  .code-body pre {
    font-size: 0.8rem;
  }
  
  .framework-card {
    padding: 16px;
  }
  
  .frameworks-grid {
    grid-template-columns: 1fr; /* Single column on small mobile screens */
    gap: 16px;
  }
}

/* SVG Utility classes */
.w-4 { width: 1rem !important; }
.h-4 { height: 1rem !important; }
.w-5 { width: 1.25rem !important; }
.h-5 { height: 1.25rem !important; }
.w-6 { width: 1.5rem !important; }
.h-6 { height: 1.5rem !important; }
.w-8 { width: 2rem !important; }
.h-8 { height: 2rem !important; }

/* Color Utilities */
.text-red-500 { color: #ef4444 !important; }
.text-red-600 { color: #dc2626 !important; }
.text-red-700 { color: #b91c1c !important; }
.text-emerald-500 { color: #10b981 !important; }
.text-sky-400 { color: #38bdf8 !important; }
.text-sky-500 { color: #0ea5e9 !important; }
.text-orange-500 { color: #f97316 !important; }
.text-orange-600 { color: #ea580c !important; }
.text-purple-600 { color: #9333ea !important; }
.text-teal-500 { color: #14b8a6 !important; }
.text-rose-500 { color: #f43f5e !important; }
.text-indigo-500 { color: #6366f1 !important; }
.text-indigo-600 { color: #4f46e5 !important; }

/* Bottom page navigation links */
.page-nav-links {
  display: flex;
  justify-content: space-between;
  gap: 16px;
  margin-top: 64px;
  padding-top: 32px;
  border-top: 1px solid var(--border-color);
}

.page-nav-link {
  flex: 1;
  display: flex;
  flex-direction: column;
  padding: 16px;
  border: 1px solid var(--border-color);
  border-radius: 12px;
  text-decoration: none;
  background-color: var(--bg-secondary);
  transition: all 0.2s;
  max-width: 48%;
}

.page-nav-link.prev {
  align-items: flex-start;
  text-align: left;
}

.page-nav-link.next {
  align-items: flex-end;
  text-align: right;
  margin-left: auto;
}

.page-nav-link:hover {
  border-color: var(--brand-color);
  background-color: var(--bg-primary);
  transform: translateY(-2px);
  box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
}

.nav-label {
  font-size: 0.75rem;
  font-weight: 600;
  color: var(--text-muted);
  text-transform: uppercase;
  margin-bottom: 4px;
}

.nav-title {
  font-size: 1rem;
  font-weight: 700;
  color: var(--brand-dark);
}

html.dark .nav-title {
  color: var(--brand-color);
}

@media (max-width: 640px) {
  .page-nav-links {
    flex-direction: column;
    gap: 12px;
    margin-top: 48px;
  }
  .page-nav-link {
    max-width: 100%;
  }
}
"""

with open("assets/index.css", "w", encoding="utf-8") as f:
    f.write(css_content)

# ----------------- Write site.js -----------------
js_content = """// Premium Javascript for responsive UI and client-side logic

document.addEventListener('DOMContentLoaded', () => {
  // Safe localStorage helper for file:// protocol and restricted environments
  const safeStorage = {
    getItem(key) {
      try {
        return localStorage.getItem(key);
      } catch (e) {
        console.warn('localStorage access denied:', e);
        return null;
      }
    },
    setItem(key, value) {
      try {
        localStorage.setItem(key, value);
      } catch (e) {
        console.warn('localStorage write denied:', e);
      }
    }
  };

  // 1. Dark Mode Toggle
  const themeToggleBtn = document.getElementById('theme-toggle');
  
  function applyTheme(theme) {
    if (theme === 'dark') {
      document.documentElement.classList.add('dark');
      if (themeToggleBtn) {
        themeToggleBtn.innerHTML = `<svg width="20" height="20" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364-6.364l-.707.707M6.343 17.657l-.707.707m0-12.728l.707.707m12.728 12.728l.707.707M12 8a4 4 0 100 8 4 4 0 000-8z"/></svg>`;
      }
    } else {
      document.documentElement.classList.remove('dark');
      if (themeToggleBtn) {
        themeToggleBtn.innerHTML = `<svg width="20" height="20" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"/></svg>`;
      }
    }
  }

  // Load saved theme safely
  let savedTheme = safeStorage.getItem('currentTheme') || 'light';
  applyTheme(savedTheme);

  if (themeToggleBtn) {
    themeToggleBtn.addEventListener('click', () => {
      savedTheme = document.documentElement.classList.contains('dark') ? 'light' : 'dark';
      safeStorage.setItem('currentTheme', savedTheme);
      applyTheme(savedTheme);
    });
  }

  // 2. Package Manager switcher logic
  const packageManager = safeStorage.getItem('packageManager') || 'npm';
  document.body.className = `pm-${packageManager}`;
  
  // Set all tab buttons active matching active package manager
  document.querySelectorAll(`.tab-btn-${packageManager}`).forEach(btn => {
    btn.classList.add('active');
  });

  window.switchPackageManager = function(pm) {
    safeStorage.setItem('packageManager', pm);
    document.body.className = `pm-${pm}`;
    
    // De-activate all tabs and active the clicked one on all step codeblocks
    document.querySelectorAll('.code-tab-btn').forEach(btn => {
      btn.classList.remove('active');
    });
    document.querySelectorAll(`.tab-btn-${pm}`).forEach(btn => {
      btn.classList.add('active');
    });
  };

  // 3. Mobile Sidebar Drawer toggle
  const menuToggleBtn = document.getElementById('menu-toggle');
  const sidebarAside = document.querySelector('.sidebar-aside');
  const sidebarBackdrop = document.getElementById('sidebar-backdrop');

  if (menuToggleBtn && sidebarAside && sidebarBackdrop) {
    menuToggleBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      sidebarAside.classList.toggle('open');
      sidebarBackdrop.classList.toggle('open');
    });
    
    sidebarBackdrop.addEventListener('click', () => {
      sidebarAside.classList.remove('open');
      sidebarBackdrop.classList.remove('open');
    });
    
    // Close sidebar on link clicks
    sidebarAside.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        sidebarAside.classList.remove('open');
        sidebarBackdrop.classList.remove('open');
      });
    });
  }

  // 4. Code Copy Button logic
  window.copyCode = function(btn, index) {
    // Find the code element inside the active block
    // We get the visible code element under the current step
    const parentCodeContainer = btn.closest('.code-container');
    const codeBlock = parentCodeContainer.querySelector('pre');
    
    if (codeBlock) {
      const textToCopy = codeBlock.innerText;
      navigator.clipboard.writeText(textToCopy).then(() => {
        btn.innerHTML = `<svg width="16" height="16" class="w-4 h-4 text-emerald-400" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>`;
        setTimeout(() => {
          btn.innerHTML = `<svg width="16" height="16" class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2m0 0h2a2 2 0 012 2v3m2 4H10m0 0l3-3m-3 3l3 3"/></svg>`;
        }, 2000);
      });
    }
  };
});
"""

with open("assets/site.js", "w", encoding="utf-8") as f:
    f.write(js_content)

# ----------------- Helper functions for HTML rendering -----------------
def generate_sidebar(active_page):
    # Categories: Getting Started, Framework Guides
    getting_started = [
        ("tailwind-cli", "Tailwind CLI"),
        ("using-postcss", "Using PostCSS"),
        ("using-vite", "Using Vite"),
        ("play-cdn", "Play CDN")
    ]
    
    frameworks = sorted(list(docs["frameworks"].keys()))
    
    sidebar_html = '<aside class="sidebar-aside">'
    
    # Section 1: Getting Started
    sidebar_html += '<div class="sidebar-nav-section"><h3>Getting Started</h3><ul class="sidebar-nav-list">'
    for slug, name in getting_started:
        active_class = " active" if active_page == slug else ""
        icon = get_icon(slug)
        sidebar_html += f'<li class="sidebar-nav-item{active_class}"><a href="{slug}.html">{icon}<span>{name}</span></a></li>'
    sidebar_html += '</ul></div>'
    
    # Section 2: Framework Guides Hub link
    active_hub = " active" if active_page == "framework-guides" else ""
    sidebar_html += '<div class="sidebar-nav-section"><h3>Guides</h3><ul class="sidebar-nav-list">'
    sidebar_html += f'<li class="sidebar-nav-item{active_hub}"><a href="framework-guides.html">{get_icon("framework-guides")}<span>Framework Guides</span></a></li>'
    sidebar_html += '</ul></div>'
    
    # Section 3: Frameworks List
    sidebar_html += '<div class="sidebar-nav-section"><h3>Frameworks</h3><ul class="sidebar-nav-list">'
    for f in frameworks:
        active_class = " active" if active_page == f else ""
        tile_title = docs["frameworks"][f]["tile"]["title"] if docs["frameworks"][f]["tile"] else f.capitalize()
        icon = get_icon(f)
        sidebar_html += f'<li class="sidebar-nav-item{active_class}"><a href="{f}.html">{icon}<span>{tile_title}</span></a></li>'
    sidebar_html += '</ul></div>'
    
    sidebar_html += '</aside>'
    return sidebar_html

def generate_header():
    return """<header>
    <div class="header-left">
      <button class="icon-btn menu-toggle" id="menu-toggle" aria-label="Toggle Menu">
        <svg width="24" height="24" class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M4 6h16M4 12h16M4 18h16"/></svg>
      </button>
      <a href="tailwind-cli.html" class="logo-link">
        <svg width="120" height="15" viewBox="0 0 167 21" fill="none" class="logo-svg" style="width: 120px;"><path class="fill-sky-400" d="M17.183 0C12.6 0 9.737 2.291 8.59 6.873c1.719-2.29 3.723-3.15 6.014-2.577 1.307.326 2.242 1.274 3.275 2.324 1.685 1.71 3.635 3.689 7.894 3.689 4.582 0 7.445-2.291 8.591-6.872-1.718 2.29-3.723 3.15-6.013 2.576-1.308-.326-2.243-1.274-3.276-2.324C23.39 1.98 21.44 0 17.183 0ZM8.59 10.309C4.01 10.309 1.145 12.6 0 17.182c1.718-2.291 3.723-3.15 6.013-2.577 1.308.326 2.243 1.274 3.276 2.324 1.685 1.71 3.635 3.689 7.894 3.689 4.582 0 7.445-2.29 8.59-6.872-1.718 2.29-3.722 3.15-6.013 2.577-1.307-.327-2.242-1.276-3.276-2.325-1.684-1.71-3.634-3.689-7.893-3.689Z" fill="#38bdf8"></path></svg>
      </a>
      <span class="version-badge">v4.3</span>
    </div>
    <div class="header-right">
      <nav class="header-nav">
        <a href="tailwind-cli.html">文档</a>
        <a href="https://tailwindcss.com/blog" target="_blank">博客</a>
        <a href="https://tailwindcss.com/showcase" target="_blank">案例展示</a>
      </nav>
      <button class="icon-btn" id="theme-toggle" aria-label="Toggle Theme">
        <svg width="20" height="20" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"/></svg>
      </button>
      <a href="https://github.com/Cayre1021/help-study" target="_blank" class="icon-btn" aria-label="GitHub Repo">
        <svg width="20" height="20" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M10 0C4.477 0 0 4.484 0 10.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.53 1.032 1.53 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0110 4.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.203 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.942.359.309.678.919.678 1.852 0 1.336-.012 2.415-.012 2.743 0 .267.18.578.688.48C17.137 18.2 20 14.44 20 10.017 20 4.484 15.522 0 10 0z"/></svg>
      </a>
    </div>
  </header>"""

# Highlighting code directives like [!code highlight]
def highlight_code_syntax(code_text, lang):
    lines = code_text.split('\n')
    highlighted = []
    i = 0
    while i < len(lines):
        line = lines[i]
        # Check if line contains highlight indicator or if NEXT line does (since Tailwind code block comments are sometimes inline or on adjacent lines)
        is_highlighted = False
        if '// [!code highlight' in line or '<!-- [!code highlight' in line or '/* [!code highlight' in line:
            is_highlighted = True
            # Clean comments
            line = re.sub(r'\s*//\s*\[!code highlight.*\]', '', line)
            line = re.sub(r'\s*<!--\s*\[!code highlight.*\]\s*-->', '', line)
            line = re.sub(r'\s*/\*\s*\[!code highlight.*\]\s*\*/', '', line)
        
        # Safe HTML escape for tags inside pre
        line_escaped = line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        
        if is_highlighted:
            highlighted.append(f'<span class="highlight-line">{line_escaped}</span>')
        else:
            highlighted.append(line_escaped)
        i += 1
    return '\n'.join(highlighted)

def build_code_block(code_name, code_lang, code_text):
    if not code_text:
        return ""
        
    # Standard code block container
    html = '<div class="code-container">'
    html += '<div class="code-header">'
    html += f'<span class="code-title">{code_name}</span>'
    
    # Render package manager switcher ONLY if code block is shell terminal and starts with npm/npx/yarn/pnpm/bun
    is_terminal = code_name == "Terminal" or code_lang == "shell"
    if is_terminal and ("npm " in code_text or "npx " in code_text or "npm install" in code_text):
        html += '<div class="code-tabs">'
        for pm in ["npm", "yarn", "pnpm", "bun"]:
            html += f'<button class="code-tab-btn code-tab-btn-{pm} tab-btn-{pm}" onclick="switchPackageManager(\'{pm}\')">{pm}</button>'
        html += '</div>'
        
    html += f'<button class="copy-btn" onclick="copyCode(this)" aria-label="Copy code"><svg width="16" height="16" class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2m0 0h2a2 2 0 012 2v3m2 4H10m0 0l3-3m-3 3l3 3"/></svg></button>'
    html += '</div>' # End code-header
    
    # If is terminal, output 4 blocks (one for each package manager), shown/hidden via CSS
    if is_terminal and ("npm " in code_text or "npx " in code_text or "npm install" in code_text):
        for pm in ["npm", "yarn", "pnpm", "bun"]:
            pm_code = translate_command(code_text, pm)
            pm_code_esc = highlight_code_syntax(pm_code, code_lang)
            html += f'<div class="code-body code-block-{pm}"><pre><code>{pm_code_esc}</code></pre></div>'
    else:
        code_esc = highlight_code_syntax(code_text, code_lang)
        html += f'<div class="code-body"><pre><code>{code_esc}</code></pre></div>'
        
    html += '</div>' # End code-container
    return html

def generate_page_nav(slug):
    getting_started = [
        ("tailwind-cli", "Tailwind CLI"),
        ("using-postcss", "Using PostCSS"),
        ("using-vite", "Using Vite"),
        ("play-cdn", "Play CDN")
    ]
    gs_slugs = [item[0] for item in getting_started]
    
    prev_link = None
    next_link = None
    
    if slug in gs_slugs:
        idx = gs_slugs.index(slug)
        if idx > 0:
            prev_link = (f"{gs_slugs[idx-1]}.html", getting_started[idx-1][1])
        if idx < len(getting_started) - 1:
            next_link = (f"{gs_slugs[idx+1]}.html", getting_started[idx+1][1])
        else:
            next_link = ("framework-guides.html", "Framework Guides")
            
    elif slug == "framework-guides":
        prev_link = ("play-cdn.html", "Play CDN")
        frameworks = sorted(list(docs["frameworks"].keys()))
        if frameworks:
            f_slug = frameworks[0]
            f_title = docs["frameworks"][f_slug]["tile"]["title"] if docs["frameworks"][f_slug]["tile"] else f_slug.capitalize()
            next_link = (f"{f_slug}.html", f_title)
            
    elif slug in docs["frameworks"]:
        frameworks = sorted(list(docs["frameworks"].keys()))
        idx = frameworks.index(slug)
        if idx > 0:
            f_slug = frameworks[idx-1]
            f_title = docs["frameworks"][f_slug]["tile"]["title"] if docs["frameworks"][f_slug]["tile"] else f_slug.capitalize()
            prev_link = (f"{f_slug}.html", f_title)
        else:
            prev_link = ("framework-guides.html", "Framework Guides")
            
        if idx < len(frameworks) - 1:
            f_slug = frameworks[idx+1]
            f_title = docs["frameworks"][f_slug]["tile"]["title"] if docs["frameworks"][f_slug]["tile"] else f_slug.capitalize()
            next_link = (f"{f_slug}.html", f_title)
        else:
            next_link = ("framework-guides.html", "Framework Guides")
            
    if not prev_link and not next_link:
        return ""
        
    nav_html = '<div class="page-nav-links">'
    if prev_link:
        url, title = prev_link
        nav_html += f'<a href="{url}" class="page-nav-link prev"><span class="nav-label">← 上一篇</span><span class="nav-title">{title}</span></a>'
    if next_link:
        url, title = next_link
        nav_html += f'<a href="{url}" class="page-nav-link next"><span class="nav-label">下一篇 →</span><span class="nav-title">{title}</span></a>'
    nav_html += '</div>'
    return nav_html

def build_guide_html(slug, data):
    title = data["title"]
    description = data["description"]
    steps = data["steps"]
    
    # Standard HTML Layout template
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} - Tailwind CSS</title>
  <meta name="description" content="{description}">
  <link rel="stylesheet" href="assets/index.css">
  <script src="assets/site.js"></script>
</head>
<body class="pm-npm">
  {generate_header()}
  <div class="sidebar-backdrop" id="sidebar-backdrop"></div>
  <div class="main-wrapper">
    {generate_sidebar(slug)}
    <main class="content-main">
      <article>
        <h1 class="page-title">{title}</h1>
        <p class="page-description">{description}</p>
        
        <div class="steps-list">
    """
    
    for idx, step in enumerate(steps):
        step_idx = idx + 1
        step_title = step["title"]
        step_body = step["body"]
        code = step["code"]
        
        code_html = build_code_block(code["name"], code["lang"], code["code"])
        
        html += f"""
          <section class="step-item">
            <div class="step-number">{step_idx}</div>
            <div class="step-header">
              <h2 class="step-title">{step_title}</h2>
            </div>
            <div class="step-body">{step_body}</div>
            {code_html}
          </section>
        """
        
    html += f"""
        </div>
        {generate_page_nav(slug)}
      </article>
    </main>
  </div>
</body>
    """
    return html

# ----------------- Write HTML Files -----------------
print("Generating static HTML pages...")

# 1. Main guides
for page, data in docs["general"].items():
    html_out = build_guide_html(page, data)
    with open(f"{page}.html", "w", encoding="utf-8") as f:
        f.write(html_out)
    print(f"Generated {page}.html")

# 2. Framework guides
for page, data in docs["frameworks"].items():
    html_out = build_guide_html(page, data)
    with open(f"{page}.html", "w", encoding="utf-8") as f:
        f.write(html_out)
    print(f"Generated {page}.html")

# 3. Create index.html (entry page, copies tailwind-cli.html)
with open("tailwind-cli.html", "r", encoding="utf-8") as f:
    cli_html = f.read()
# Replace relative paths or active sidebar states to point to tailwind-cli
with open("index.html", "w", encoding="utf-8") as f:
    f.write(cli_html)
print("Generated index.html (entry page)")

# 4. Create framework-guides.html hub page
hub_title = "Framework Guides"
hub_description = "Explore our framework guides to get set up with Tailwind CSS."
hub_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{hub_title} - Tailwind CSS</title>
  <meta name="description" content="{hub_description}">
  <link rel="stylesheet" href="assets/index.css">
  <script src="assets/site.js"></script>
</head>
<body class="pm-npm">
  {generate_header()}
  <div class="sidebar-backdrop" id="sidebar-backdrop"></div>
  <div class="main-wrapper">
    {generate_sidebar("framework-guides")}
    <main class="content-main">
      <article>
        <h1 class="page-title">{hub_title}</h1>
        <p class="page-description">{hub_description}</p>
        
        <div class="frameworks-grid">
"""

for slug, data in sorted(docs["frameworks"].items()):
    tile = data["tile"]
    if tile:
        t_title = tile["title"]
        t_desc = tile["description"]
    else:
        t_title = slug.capitalize()
        t_desc = f"Setting up Tailwind CSS in a {t_title} project."
        
    icon_svg = get_icon(slug)
    hub_html += f"""
          <a href="{slug}.html" class="framework-card">
            <div class="framework-card-header">
              {icon_svg}
              <h2 class="framework-card-title">{t_title}</h2>
            </div>
            <p class="framework-card-desc">{t_desc}</p>
          </a>
    """

hub_html += f"""
        </div>
        {generate_page_nav("framework-guides")}
      </article>
    </main>
  </div>
</body>
</html>
"""

with open("framework-guides.html", "w", encoding="utf-8") as f:
    f.write(hub_html)
print("Generated framework-guides.html")


# ----------------- Generate tailwind_docs.md -----------------
print("Generating tailwind_docs.md...")

md_out = """# Tailwind CSS v4.3 安装指南 (Scope A)

此文档包含从官方文档直接编译的所有 Tailwind CSS 安装指南和框架设置说明的合并集合。

## 目录

- [常规指南](#常规指南)
  - [Tailwind CLI](#tailwind-cli)
  - [Using PostCSS](#using-postcss)
  - [Using Vite](#using-vite)
  - [Play CDN](#play-cdn)
- [框架特定指南](#框架特定指南)
"""

for slug in sorted(docs["frameworks"].keys()):
    tile_title = docs["frameworks"][slug]["tile"]["title"] if docs["frameworks"][slug]["tile"] else slug.capitalize()
    md_out += f"  - [{tile_title}](#{slug})\n"

md_out += "\n---\n\n## <a id=\"常规指南\"></a>常规指南\n\n"

# Render General guides in markdown
for page in ["tailwind-cli", "using-postcss", "using-vite", "play-cdn"]:
    data = docs["general"][page]
    md_out += f"### {data['title']}\n\n"
    md_out += f"{data['description']}\n\n"
    
    for idx, step in enumerate(data["steps"]):
        md_out += f"#### 步骤 {idx+1}: {step['title']}\n\n"
        # Convert simple html in body to clean markdown
        body_md = step["body"].replace("<p>", "").replace("</p>", "").strip()
        body_md = re.sub(r'<code>(.*?)</code>', r'`\1`', body_md)
        body_md = re.sub(r'<a href="([^"]*)">(.*?)</a>', r'[\2](\1)', body_md)
        body_md = body_md.replace("", "'")
        md_out += f"{body_md}\n\n"
        
        code = step["code"]
        if code["code"]:
            md_out += f"*{code['name']}*\n"
            md_out += f"```{code['lang']}\n{code['code']}\n```\n\n"
    md_out += "---\n\n"

md_out += "## <a id=\"框架特定指南\"></a>框架特定指南\n\n"

# Render Framework guides in markdown
for page in sorted(docs["frameworks"].keys()):
    data = docs["frameworks"][page]
    md_out += f"### <a id=\"{page}\"></a>{data['title']}\n\n"
    md_out += f"{data['description']}\n\n"
    
    for idx, step in enumerate(data["steps"]):
        md_out += f"#### 步骤 {idx+1}: {step['title']}\n\n"
        body_md = step["body"].replace("<p>", "").replace("</p>", "").strip()
        body_md = re.sub(r'<code>(.*?)</code>', r'`\1`', body_md)
        body_md = re.sub(r'<a href="([^"]*)">(.*?)</a>', r'[\2](\1)', body_md)
        body_md = body_md.replace("", "'")
        md_out += f"{body_md}\n\n"
        
        code = step["code"]
        if code["code"]:
            md_out += f"*{code['name']}*\n"
            md_out += f"```{code['lang']}\n{code['code']}\n```\n\n"
    md_out += "---\n\n"

with open("tailwind_docs.md", "w", encoding="utf-8") as f:
    f.write(md_out)
print("Generated tailwind_docs.md")
print("All docs generation completed successfully!")
