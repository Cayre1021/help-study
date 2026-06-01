# Tailwind CSS v4.0 Installation Guides (Scope A)

This document contains a consolidated collection of all Tailwind CSS installation guides and framework setup instructions compiled directly from the official documentation.

## Table of Contents

- [General Guides](#general-guides)
  - [Tailwind CLI](#tailwind-cli)
  - [Using PostCSS](#using-postcss)
  - [Using Vite](#using-vite)
  - [Play CDN](#play-cdn)
- [Framework-Specific Guides](#framework-specific-guides)
  - [AdonisJS](#adonisjs)
  - [Angular](#angular)
  - [Astro](#astro)
  - [Ember.js](#emberjs)
  - [Gatsby](#gatsby)
  - [Laravel](#laravel)
  - [Meteor](#meteor)
  - [Next.js](#nextjs)
  - [Nuxt](#nuxtjs)
  - [Parcel](#parcel)
  - [Phoenix](#phoenix)
  - [Qwik](#qwik)
  - [React Router](#react-router)
  - [Rspack](#rspack)
  - [Ruby on Rails](#ruby-on-rails)
  - [SolidJS](#solidjs)
  - [SvelteKit](#sveltekit)
  - [Symfony](#symfony)
  - [TanStack Start](#tanstack-start)

---

## General Guides

### Tailwind CLI

The simplest and fastest way to get up and running with Tailwind CSS from scratch is with the Tailwind CLI tool.

#### Step 1: Install Tailwind CSS

'I'n's't'a'l'l' '`'t'a'i'l'w'i'n'd'c's's'`' 'a'n'd' '`'@'t'a'i'l'w'i'n'd'c's's'/'c'l'i'`' 'v'i'a' 'n'p'm'.'

#### Step 2: Import Tailwind in your CSS

'A'd'd' 't'h'e' '`'@'i'm'p'o'r't' '"'t'a'i'l'w'i'n'd'c's's'"';'`' 'i'm'p'o'r't' 't'o' 'y'o'u'r' 'm'a'i'n' 'C'S'S' 'f'i'l'e'.'

#### Step 3: Start the Tailwind CLI build process

'R'u'n' 't'h'e' 'C'L'I' 't'o'o'l' 't'o' 's'c'a'n' 'y'o'u'r' 's'o'u'r'c'e' 'f'i'l'e's' 'f'o'r' 'c'l'a's's'e's' 'a'n'd' 'b'u'i'l'd' 'y'o'u'r' 'C'S'S'.'

#### Step 4: Start using Tailwind in your HTML

'A'd'd' 'y'o'u'r' 'c'o'm'p'i'l'e'd' 'C'S'S' 'f'i'l'e' 't'o' 't'h'e' '`'<'h'e'a'd'>'`' 'a'n'd' 's't'a'r't' 'u's'i'n'g' 'T'a'i'l'w'i'n'd'''s' 'u't'i'l'i't'y' 'c'l'a's's'e's' 't'o' 's't'y'l'e' 'y'o'u'r' 'c'o'n't'e'n't'.'

*src/index.html*
```html
<!doctype html>
        <html>
        <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <!-- [!code highlight:2] -->
          <link href="./output.css" rel="stylesheet">
        </head>
        <body>
          <!-- [!code highlight:4] -->
          <h1 class="text-3xl font-bold underline">
            Hello world!
          </h1>
        </body>
        </html>
```

---

### Installing Tailwind CSS with PostCSS

Installing Tailwind CSS as a PostCSS plugin is the most seamless way to integrate it with frameworks like Next.js and Angular.

#### Step 1: Install Tailwind CSS

'I'n's't'a'l'l' '`'t'a'i'l'w'i'n'd'c's's'`',' '`'@'t'a'i'l'w'i'n'd'c's's'/'p'o's't'c's's'`',' 'a'n'd' '`'p'o's't'c's's'`' 'v'i'a' 'n'p'm'.'

*Terminal*
```shell
npm install tailwindcss @tailwindcss/postcss postcss
```

#### Step 2: Add Tailwind to your PostCSS configuration

'A'd'd' '`'@'t'a'i'l'w'i'n'd'c's's'/'p'o's't'c's's'`' 't'o' 'y'o'u'r' '`'p'o's't'c's's'.'c'o'n'f'i'g'.'m'j's'`' 'f'i'l'e',' 'o'r' 'w'h'e'r'e'v'e'r' 'P'o's't'C'S'S' 'i's' 'c'o'n'f'i'g'u'r'e'd' 'i'n' 'y'o'u'r' 'p'r'o'j'e'c't'.'

*postcss.config.mjs*
```js
export default {
          plugins: {
            // [!code highlight:2]
            "@tailwindcss/postcss": {},
          }
        }
```

#### Step 3: Import Tailwind CSS

'A'd'd' 'a'n' '`'@'i'm'p'o'r't'`' 't'o' 'y'o'u'r' 'C'S'S' 'f'i'l'e' 't'h'a't' 'i'm'p'o'r't's' 'T'a'i'l'w'i'n'd' 'C'S'S'.'

*CSS*
```css
@import "tailwindcss";
```

#### Step 4: Start your build process

'R'u'n' 'y'o'u'r' 'b'u'i'l'd' 'p'r'o'c'e's's' 'w'i't'h' '`'n'p'm' 'r'u'n' 'd'e'v'`' 'o'r' 'w'h'a't'e'v'e'r' 'c'o'm'm'a'n'd' 'i's' 'c'o'n'f'i'g'u'r'e'd' 'i'n' 'y'o'u'r' '`'p'a'c'k'a'g'e'.'j's'o'n'`' 'f'i'l'e'.'

*Terminal*
```shell
npm run dev
```

#### Step 5: Start using Tailwind in your HTML

'M'a'k'e' 's'u'r'e' 'y'o'u'r' 'c'o'm'p'i'l'e'd' 'C'S'S' 'i's' 'i'n'c'l'u'd'e'd' 'i'n' 't'h'e' '`'<'h'e'a'd'>'`'<'e'm'>'('y'o'u'r' 'f'r'a'm'e'w'o'r'k' 'm'i'g'h't' 'h'a'n'd'l'e' 't'h'i's' 'f'o'r' 'y'o'u')'<'/'e'm'>',' 't'h'e'n' 's't'a'r't' 'u's'i'n'g' 'T'a'i'l'w'i'n'd'''s' 'u't'i'l'i't'y' 'c'l'a's's'e's' 't'o' 's't'y'l'e' 'y'o'u'r' 'c'o'n't'e'n't'.'

*HTML*
```html
<!doctype html>
        <html>
        <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <!-- [!code highlight:2] -->
          <link href="/dist/styles.css" rel="stylesheet">
        </head>
        <body>
          <!-- [!code highlight:4] -->
          <h1 class="text-3xl font-bold underline">
            Hello world!
          </h1>
        </body>
        </html>
```

---

### Installing Tailwind CSS with Vite

Installing Tailwind CSS as a Vite plugin is the most seamless way to integrate it with frameworks like Laravel, SvelteKit, React Router, Nuxt, and SolidJS.

#### Step 1: Create your project

'S't'a'r't' 'b'y' 'c'r'e'a't'i'n'g' 'a' 'n'e'w' 'V'i't'e' 'p'r'o'j'e'c't' 'i'f' 'y'o'u' 'd'o'n'''t' 'h'a'v'e' 'o'n'e' 's'e't' 'u'p' 'a'l'r'e'a'd'y'.' 'T'h'e' 'm'o's't' 'c'o'm'm'o'n' 'a'p'p'r'o'a'c'h' 'i's' 't'o' 'u's'e' '['C'r'e'a't'e' 'V'i't'e']'('h't't'p's':'/'/'v'i't'e'.'d'e'v'/'g'u'i'd'e'/'#'s'c'a'f'f'o'l'd'i'n'g'-'y'o'u'r'-'f'i'r's't'-'v'i't'e'-'p'r'o'j'e'c't')'.'

*Terminal*
```shell
npm create vite@latest my-project
        cd my-project
```

#### Step 2: Install Tailwind CSS

'I'n's't'a'l'l' '`'t'a'i'l'w'i'n'd'c's's'`' 'a'n'd' '`'@'t'a'i'l'w'i'n'd'c's's'/'v'i't'e'`' 'v'i'a' 'n'p'm'.'

*Terminal*
```shell
npm install tailwindcss @tailwindcss/vite
```

#### Step 3: Configure the Vite plugin

'A'd'd' 't'h'e' '`'@'t'a'i'l'w'i'n'd'c's's'/'v'i't'e'`' 'p'l'u'g'i'n' 't'o' 'y'o'u'r' 'V'i't'e' 'c'o'n'f'i'g'u'r'a't'i'o'n'.'

*vite.config.ts*
```js
import { defineConfig } from 'vite'
        // [!code highlight:2]
        import tailwindcss from '@tailwindcss/vite'

        export default defineConfig({
          plugins: [
            // [!code highlight:2]
            tailwindcss(),
          ],
        })
```

#### Step 4: Import Tailwind CSS

'A'd'd' 'a'n' '`'@'i'm'p'o'r't'`' 't'o' 'y'o'u'r' 'C'S'S' 'f'i'l'e' 't'h'a't' 'i'm'p'o'r't's' 'T'a'i'l'w'i'n'd' 'C'S'S'.'

*CSS*
```css
@import "tailwindcss";
```

#### Step 5: Start your build process

'R'u'n' 'y'o'u'r' 'b'u'i'l'd' 'p'r'o'c'e's's' 'w'i't'h' '`'n'p'm' 'r'u'n' 'd'e'v'`' 'o'r' 'w'h'a't'e'v'e'r' 'c'o'm'm'a'n'd' 'i's' 'c'o'n'f'i'g'u'r'e'd' 'i'n' 'y'o'u'r' '`'p'a'c'k'a'g'e'.'j's'o'n'`' 'f'i'l'e'.'

*Terminal*
```shell
npm run dev
```

#### Step 6: Start using Tailwind in your HTML

'M'a'k'e' 's'u'r'e' 'y'o'u'r' 'c'o'm'p'i'l'e'd' 'C'S'S' 'i's' 'i'n'c'l'u'd'e'd' 'i'n' 't'h'e' '`'<'h'e'a'd'>'`'<'e'm'>'('y'o'u'r' 'f'r'a'm'e'w'o'r'k' 'm'i'g'h't' 'h'a'n'd'l'e' 't'h'i's' 'f'o'r' 'y'o'u')'<'/'e'm'>',' 't'h'e'n' 's't'a'r't' 'u's'i'n'g' 'T'a'i'l'w'i'n'd'''s' 'u't'i'l'i't'y' 'c'l'a's's'e's' 't'o' 's't'y'l'e' 'y'o'u'r' 'c'o'n't'e'n't'.'

*HTML*
```html
<!doctype html>
        <html>
        <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <!-- [!code highlight:2] -->
          <link href="/src/style.css" rel="stylesheet">
        </head>
        <body>
          <!-- [!code highlight:4] -->
          <h1 class="text-3xl font-bold underline">
            Hello world!
          </h1>
        </body>
        </html>
```

---

### Play CDN

Use the Play CDN to try Tailwind right in the browser without any build step.

#### Step 1: Add the Play CDN script to your HTML

'A'd'd' 't'h'e' 'P'l'a'y' 'C'D'N' 's'c'r'i'p't' 't'a'g' 't'o' 't'h'e' '`'&'l't';'h'e'a'd'&'g't';'`' 'o'f' 'y'o'u'r' 'H'T'M'L' 'f'i'l'e',' 'a'n'd' 's't'a'r't' 'u's'i'n'g' 'T'a'i'l'w'i'n'd'''s' 'u't'i'l'i't'y' 'c'l'a's's'e's' 't'o' 's't'y'l'e' 'y'o'u'r' 'c'o'n't'e'n't'.'

*index.html*
```html
<!doctype html>
        <html>
          <head>
            <meta charset="UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <!-- [!code highlight:2] -->
            <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
          </head>
          <body>
            <!-- [!code highlight:4] -->
            <h1 class="text-3xl font-bold underline">
              Hello world!
            </h1>
          </body>
        </html>
```

#### Step 2: Try adding some custom CSS

'U's'e' '`'t'y'p'e'='"'t'e'x't'/'t'a'i'l'w'i'n'd'c's's'"'`' 't'o' 'a'd'd' 'c'u's't'o'm' 'C'S'S' 't'h'a't' 's'u'p'p'o'r't's' 'a'l'l' 'o'f' 'T'a'i'l'w'i'n'd'''s' 'C'S'S' 'f'e'a't'u'r'e's'.'

*index.html*
```html
<!doctype html>
        <html>
          <head>
            <meta charset="UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
            <!-- [!code highlight:6] -->
            <style type="text/tailwindcss">
              @theme {
                --color-clifford: #da373d;
              }
            </style>
          </head>
          <body>
            <!-- [!code word:text-clifford] -->
            <h1 class="text-3xl font-bold underline text-clifford">
              Hello world!
            </h1>
          </body>
        </html>
```

---

## Framework-Specific Guides

### <a id="adonisjs"></a>Install Tailwind CSS with AdonisJS

Setting up Tailwind CSS in an AdonisJS project.

#### Step 1: Create your project

'S't'a'r't' 'b'y' 'c'r'e'a't'i'n'g' 'a' 'n'e'w' 'A'd'o'n'i's'J'S' 'p'r'o'j'e'c't' 'i'f' 'y'o'u' 'd'o'n'''t' 'h'a'v'e' 'o'n'e' 's'e't' 'u'p' 'a'l'r'e'a'd'y'.' 'T'h'e' 'm'o's't' 'c'o'm'm'o'n' 'a'p'p'r'o'a'c'h' 'i's' 't'o' 'u's'e' '['C'r'e'a't'e' 'A'd'o'n'i's'J'S']'('h't't'p's':'/'/'d'o'c's'.'a'd'o'n'i's'j's'.'c'o'm'/'g'u'i'd'e's'/'g'e't't'i'n'g'-'s't'a'r't'e'd'/'i'n's't'a'l'l'a't'i'o'n')'.'

*Terminal*
```shell
npm init adonisjs@latest my-project -- --kit=web
        cd my-project
```

#### Step 2: Install Tailwind CSS

'I'n's't'a'l'l' '`'@'t'a'i'l'w'i'n'd'c's's'/'v'i't'e'`' 'a'n'd' 'i't's' 'p'e'e'r' 'd'e'p'e'n'd'e'n'c'i'e's' 'v'i'a' 'n'p'm'.'

*Terminal*
```shell
npm install tailwindcss @tailwindcss/vite
```

#### Step 3: Configure Vite Plugin

'A'd'd' 't'h'e' '`'@'t'a'i'l'w'i'n'd'c's's'/'v'i't'e'`' 'p'l'u'g'i'n' 't'o' 'y'o'u'r' 'V'i't'e' 'c'o'n'f'i'g'u'r'a't'i'o'n'.'

*vite.config.ts*
```ts
import { defineConfig } from 'vite'
        import adonisjs from '@adonisjs/vite/client'
        // [!code highlight:2]
        import tailwindcss from '@tailwindcss/vite'

        export default defineConfig({
          plugins: [
            // [!code highlight:2]
            tailwindcss(),
            adonisjs({
              // …
            }),
          ],
        })
```

#### Step 4: Import Tailwind CSS

'A'd'd' 'a'n' '`'@'i'm'p'o'r't'`' 't'o' '`'.'/'r'e's'o'u'r'c'e's'/'c's's'/'a'p'p'.'c's's'`' 't'h'a't' 'i'm'p'o'r't's' 'T'a'i'l'w'i'n'd' 'C'S'S'''s' 's't'y'l'e's'.' 'A'd'd'i't'i'o'n'a'l'l'y',' 't'e'l'l' 'T'a'i'l'w'i'n'd' 'C'S'S' 't'o' 's'c'a'n' 'y'o'u'r' '`'r'e's'o'u'r'c'e's'/'v'i'e'w's'`' 'd'i'r'e'c't'o'r'y' 'f'o'r' 'u't'i'l'i't'i'e's'.'

*app.css*
```css
@import "tailwindcss";
        @source "../views";
```

#### Step 5: Start your build process

'R'u'n' 'y'o'u'r' 'b'u'i'l'd' 'p'r'o'c'e's's' 'w'i't'h' '`'n'p'm' 'r'u'n' 'd'e'v'`'.'

#### Step 6: Start using Tailwind in your project

'M'a'k'e' 's'u'r'e' 'y'o'u'r' 'c'o'm'p'i'l'e'd' 'C'S'S' 'i's' 'i'n'c'l'u'd'e'd' 'i'n' 't'h'e' '`'<'h'e'a'd'>'`' 't'h'e'n' 's't'a'r't' 'u's'i'n'g' 'T'a'i'l'w'i'n'd'''s' 'u't'i'l'i't'y' 'c'l'a's's'e's' 't'o' 's't'y'l'e' 'y'o'u'r' 'c'o'n't'e'n't'.'

*home.edge*
```edge
<!doctype html>
        <html>
          <head>
            <meta charset="utf-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <!-- [!code highlight:2] -->
            @vite(['resources/css/app.css', 'resources/js/app.js'])
          </head>
          <body>
            <!-- [!code highlight:4] -->
            <h1 class="text-3xl font-bold underline">
              <!-- prettier-ignore -->
              Hello world!
            </h1>
          </body>
        </html>
```

---

### <a id="angular"></a>Install Tailwind CSS with Angular

Setting up Tailwind CSS in an Angular project.

#### Step 1: Create your project

'S't'a'r't' 'b'y' 'c'r'e'a't'i'n'g' 'a' 'n'e'w' 'A'n'g'u'l'a'r' 'p'r'o'j'e'c't' 'i'f' 'y'o'u' 'd'o'n'''t' 'h'a'v'e' 'o'n'e' 's'e't' 'u'p' 'a'l'r'e'a'd'y'.' 'T'h'e' 'm'o's't' 'c'o'm'm'o'n' 'a'p'p'r'o'a'c'h' 'i's' 't'o' 'u's'e' '['A'n'g'u'l'a'r' 'C'L'I']'('h't't'p's':'/'/'a'n'g'u'l'a'r'.'d'e'v'/'t'o'o'l's'/'c'l'i'/'s'e't'u'p'-'l'o'c'a'l')'.'

*Terminal*
```shell
ng new my-project --style css
        cd my-project
```

#### Step 2: Install Tailwind CSS

'(' ' 'I'n's't'a'l'l' '`'@'t'a'i'l'w'i'n'd'c's's'/'p'o's't'c's's'`' 'a'n'd' 'i't's' 'p'e'e'r' 'd'e'p'e'n'd'e'n'c'i'e's' 'v'i'a' 'n'p'm'.' ' ')',' '/'/' 'N'O'T'E':' 'T'h'e' '`'-'-'f'o'r'c'e'`' 'f'l'a'g' 'i's' 'u's'e'd' 't'o' 'm'a'k'e' 's'u'r'e' 't'h'e' 'i'n's't'a'l'l'a't'i'o'n' 's'u'c'c'e'e'd's'.' 'A'n'g'u'l'a'r' 'h'a's' 'a' 'p'e'e'r' 'd'e'p'e'n'd'e'n'c'y' 'o'n' '`'t'a'i'l'w'i'n'd'c's's'`' 'v'3' 'w'h'i'c'h' 'c'a'u's'e's' 'e'r'r'o'r's' 'w'h'e'n' 'i'n's't'a'l'l'i'n'g' '`'t'a'i'l'w'i'n'd'c's's'`' 'v'4'.' 'c'o'd'e':' '{' 'n'a'm'e':' '"'T'e'r'm'i'n'a'l'"',' 'l'a'n'g':' '"'s'h'e'l'l'"'

*Terminal*
```shell
npm install tailwindcss @tailwindcss/postcss postcss --force
```

#### Step 3: Configure PostCSS Plugins

'C'r'e'a't'e' 'a' '`'.'p'o's't'c's's'r'c'.'j's'o'n'`' 'f'i'l'e' 'i'n' 't'h'e' 'r'o'o't' 'o'f' 'y'o'u'r' 'p'r'o'j'e'c't' 'a'n'd' 'a'd'd' 't'h'e' '`'@'t'a'i'l'w'i'n'd'c's's'/'p'o's't'c's's'`' 'p'l'u'g'i'n' 't'o' 'y'o'u'r' 'P'o's't'C'S'S' 'c'o'n'f'i'g'u'r'a't'i'o'n'.'

*.postcssrc.json*
```js
{
          "plugins": {
            // [!code highlight:2]
            "@tailwindcss/postcss": {}
          }
        }
```

#### Step 4: Import Tailwind CSS

'A'd'd' 'a'n' '`'@'i'm'p'o'r't'`' 't'o' '`'.'/'s'r'c'/'s't'y'l'e's'.'c's's'`' 't'h'a't' 'i'm'p'o'r't's' 'T'a'i'l'w'i'n'd' 'C'S'S'.'

*styles.css*
```css
@import "tailwindcss";
```

#### Step 5: Start your build process

'R'u'n' 'y'o'u'r' 'b'u'i'l'd' 'p'r'o'c'e's's' 'w'i't'h' '`'n'g' 's'e'r'v'e'`'.'

*Terminal*
```shell
ng serve
```

#### Step 6: Start using Tailwind in your project

'S't'a'r't' 'u's'i'n'g' 'T'a'i'l'w'i'n'd'''s' 'u't'i'l'i't'y' 'c'l'a's's'e's' 't'o' 's't'y'l'e' 'y'o'u'r' 'c'o'n't'e'n't'.'

*app.component.html*
```html
<!-- [!code highlight:4] -->
        <h1 class="text-3xl font-bold underline">
          <!-- prettier-ignore -->
          Hello world!
        </h1>
```

---

### <a id="astro"></a>Install Tailwind CSS with Astro

Setting up Tailwind CSS in an Astro project.

#### Step 1: Create your project

'S't'a'r't' 'b'y' 'c'r'e'a't'i'n'g' 'a' 'n'e'w' 'A's't'r'o' 'p'r'o'j'e'c't' 'i'f' 'y'o'u' 'd'o'n'''t' 'h'a'v'e' 'o'n'e' 's'e't' 'u'p' 'a'l'r'e'a'd'y'.' 'T'h'e' 'm'o's't' 'c'o'm'm'o'n' 'a'p'p'r'o'a'c'h' 'i's' 't'o' 'u's'e' '['c'r'e'a't'e' 'a's't'r'o']'('h't't'p's':'/'/'d'o'c's'.'a's't'r'o'.'b'u'i'l'd'/'e'n'/'i'n's't'a'l'l'-'a'n'd'-'s'e't'u'p'/'#'i'n's't'a'l'l'-'f'r'o'm'-'t'h'e'-'c'l'i'-'w'i'z'a'r'd')'.'

*Terminal*
```shell
npm create astro@latest my-project
        cd my-project
```

#### Step 2: Install Tailwind CSS

'I'n's't'a'l'l' '`'@'t'a'i'l'w'i'n'd'c's's'/'v'i't'e'`' 'a'n'd' 'i't's' 'p'e'e'r' 'd'e'p'e'n'd'e'n'c'i'e's' 'v'i'a' 'n'p'm'.'

*Terminal*
```shell
npm install tailwindcss @tailwindcss/vite
```

#### Step 3: Configure Vite Plugin

'A'd'd' 't'h'e' '`'@'t'a'i'l'w'i'n'd'c's's'/'v'i't'e'`' 'p'l'u'g'i'n' 't'o' 'y'o'u'r' 'V'i't'e' 'p'l'u'g'i'n's' 'i'n' 'y'o'u'r' 'A's't'r'o' 'c'o'n'f'i'g' 'f'i'l'e'.'

*astro.config.mjs*
```js
// @ts-check
        import { defineConfig } from "astro/config";
        // [!code highlight:2]
        import tailwindcss from "@tailwindcss/vite";

        // https://astro.build/config
        export default defineConfig({
          // [!code highlight:4]
          vite: {
            plugins: [tailwindcss()],
          },
        });
```

#### Step 4: Import Tailwind CSS

'C'r'e'a't'e' 'a' '`'.'/'s'r'c'/'s't'y'l'e's'/'g'l'o'b'a'l'.'c's's'`' 'f'i'l'e' 'a'n'd' 'a'd'd' 'a'n' '`'@'i'm'p'o'r't'`' 'f'o'r' 'T'a'i'l'w'i'n'd' 'C'S'S'.'

*global.css*
```css
@import "tailwindcss";
```

#### Step 5: Start your build process

'R'u'n' 'y'o'u'r' 'b'u'i'l'd' 'p'r'o'c'e's's' 'w'i't'h' '`'n'p'm' 'r'u'n' 'd'e'v'`'.'

*Terminal*
```shell
npm run dev
```

#### Step 6: Start using Tailwind in your project

'S't'a'r't' 'u's'i'n'g' 'T'a'i'l'w'i'n'd'''s' 'u't'i'l'i't'y' 'c'l'a's's'e's' 't'o' 's't'y'l'e' 'y'o'u'r' 'c'o'n't'e'n't' 'w'h'i'l'e' 'm'a'k'i'n'g' 's'u'r'e' 't'o' 'i'm'p'o'r't' 't'h'e' 'n'e'w'l'y' 'c'r'e'a't'e'd' 'C'S'S' 'f'i'l'e'.'

---

### <a id="emberjs"></a>Install Tailwind CSS with Ember.js

Setting up Tailwind CSS in an Ember.js project.

#### Step 1: Create your project

'S't'a'r't' 'b'y' 'c'r'e'a't'i'n'g' 'a' 'n'e'w' 'E'm'b'e'r'.'j's' 'p'r'o'j'e'c't' 'i'f' 'y'o'u' 'd'o'n'''t' 'h'a'v'e' 'o'n'e' 's'e't' 'u'p' 'a'l'r'e'a'd'y'.' 'T'h'e' 'm'o's't' 'c'o'm'm'o'n' 'a'p'p'r'o'a'c'h' 'i's' 't'o' 'u's'e' '[' 'E'm'b'e'r' 'C'L'I' ']'('h't't'p's':'/'/'g'u'i'd'e's'.'e'm'b'e'r'j's'.'c'o'm'/'r'e'l'e'a's'e'/'g'e't't'i'n'g'-'s't'a'r't'e'd'/'q'u'i'c'k'-'s't'a'r't'/'#'t'o'c'_'c'r'e'a't'e'-'a'-'n'e'w'-'a'p'p'l'i'c'a't'i'o'n')' '.'

*Terminal*
```shell
npx ember-cli new my-project --embroider --no-welcome
        cd my-project
```

#### Step 2: Install Tailwind CSS

'U's'i'n'g' 'n'p'm',' 'i'n's't'a'l'l' '`'@'t'a'i'l'w'i'n'd'c's's'/'p'o's't'c's's'`' 'a'n'd' 'i't's' 'p'e'e'r' 'd'e'p'e'n'd'e'n'c'i'e's',' 'a's' 'w'e'l'l' 'a's' '`'p'o's't'c's's'-'l'o'a'd'e'r'`'.'

*Terminal*
```shell
npm install tailwindcss @tailwindcss/postcss postcss postcss-loader
```

#### Step 3: Enable PostCSS support

'I'n' 'y'o'u'r' '`'e'm'b'e'r'-'c'l'i'-'b'u'i'l'd'.'j's'`' 'f'i'l'e',' 'c'o'n'f'i'g'u'r'e' 'P'o's't'C'S'S' 't'o' 'p'r'o'c'e's's' 'y'o'u'r' 'C'S'S' 'f'i'l'e's'.'

*ember-cli-build.js*
```js
'use strict';

        const EmberApp = require('ember-cli/lib/broccoli/ember-app');

        module.exports = function (defaults) {
          const app = new EmberApp(defaults, {
            // Add options here
          });

          const { Webpack } = require('@embroider/webpack');
          return require('@embroider/compat').compatBuild(app, Webpack, {
            skipBabel: [
              {
                package: 'qunit',
              },
            ],
            // [!code highlight:22]
            packagerOptions: {
              webpackConfig: {
                module: {
                  rules: [
                    {
                      test: /\.css$/i,
                      use: ['postcss-loader'],
                    },
                  ],
                },
              },
            },
          });
        };
```

#### Step 4: Configure PostCSS Plugins

'C'r'e'a't'e' 'a' '`'p'o's't'c's's'.'c'o'n'f'i'g'.'m'j's'`' 'f'i'l'e' 'i'n' 't'h'e' 'r'o'o't' 'o'f' 'y'o'u'r' 'p'r'o'j'e'c't' 'a'n'd' 'a'd'd' 't'h'e' '`'@'t'a'i'l'w'i'n'd'c's's'/'p'o's't'c's's'`' 'p'l'u'g'i'n' 't'o' 'y'o'u'r' 'P'o's't'C'S'S' 'c'o'n'f'i'g'u'r'a't'i'o'n'.'

*postcss.config.mjs*
```js
export default {
          plugins: {
            // [!code highlight:2]
            "@tailwindcss/postcss": {},
          },
        }
```

#### Step 5: Import Tailwind CSS

'C'r'e'a't'e' 'a'n' '`'.'/'a'p'p'/'a'p'p'.'c's's'`' 'f'i'l'e' 'a'n'd' 'a'd'd' 'a'n' '`'@'i'm'p'o'r't'`' 'f'o'r' 'T'a'i'l'w'i'n'd' 'C'S'S'.'

*app.css*
```css
@import "tailwindcss";
```

#### Step 6: Import the CSS file

'I'm'p'o'r't' 't'h'e' 'n'e'w'l'y'-'c'r'e'a't'e'd' '`'.'/'a'p'p'/'a'p'p'.'c's's'`' 'f'i'l'e' 'i'n' 'y'o'u'r' '`'.'/'a'p'p'/'a'p'p'.'j's'`' 'f'i'l'e'.'

*app.js*
```js
import Application from '@ember/application';
        import Resolver from 'ember-resolver';
        import loadInitializers from 'ember-load-initializers';
        import config from 'my-project/config/environment';
        // [!code highlight:2]
        import 'my-project/app.css';

        export default class App extends Application {
          modulePrefix = config.modulePrefix;
          podModulePrefix = config.podModulePrefix;
          Resolver = Resolver;
        }

        loadInitializers(App, config.modulePrefix);
```

#### Step 7: Start your build process

'R'u'n' 'y'o'u'r' 'b'u'i'l'd' 'p'r'o'c'e's's' 'w'i't'h' '`'n'p'm' 'r'u'n' 's't'a'r't'`'.'

*Terminal*
```shell
npm run start
```

#### Step 8: Start using Tailwind in your project

'S't'a'r't' 'u's'i'n'g' 'T'a'i'l'w'i'n'd'''s' 'u't'i'l'i't'y' 'c'l'a's's'e's' 't'o' 's't'y'l'e' 'y'o'u'r' 'c'o'n't'e'n't'.'

---

### <a id="gatsby"></a>Install Tailwind CSS with Gatsby

Setting up Tailwind CSS in a Gatsby project.

#### Step 1: Create your project

'S't'a'r't' 'b'y' 'c'r'e'a't'i'n'g' 'a' 'n'e'w' 'G'a't's'b'y' 'p'r'o'j'e'c't' 'i'f' 'y'o'u' 'd'o'n'''t' 'h'a'v'e' 'o'n'e' 's'e't' 'u'p' 'a'l'r'e'a'd'y'.' 'T'h'e' 'm'o's't' 'c'o'm'm'o'n' 'a'p'p'r'o'a'c'h' 'i's' 't'o' 'u's'e' '['G'a't's'b'y' 'C'L'I']'('h't't'p's':'/'/'w'w'w'.'g'a't's'b'y'j's'.'c'o'm'/'d'o'c's'/'r'e'f'e'r'e'n'c'e'/'g'a't's'b'y'-'c'l'i'/'#'h'o'w'-'t'o'-'u's'e'-'g'a't's'b'y'-'c'l'i')'.'

*Terminal*
```shell
gatsby new my-project
        cd my-project
```

#### Step 2: Install Tailwind CSS

'U's'i'n'g' 'n'p'm',' 'i'n's't'a'l'l' '`'@'t'a'i'l'w'i'n'd'c's's'/'p'o's't'c's's'`',' 'i't's' 'p'e'e'r' 'd'e'p'e'n'd'e'n'c'i'e's',' 'a'n'd' '`'g'a't's'b'y'-'p'l'u'g'i'n'-'p'o's't'c's's'`'.'

*Terminal*
```shell
npm install @tailwindcss/postcss tailwindcss postcss gatsby-plugin-postcss
```

#### Step 3: Enable the Gatsby PostCSS plugin

'I'n' 'y'o'u'r' '`'g'a't's'b'y'-'c'o'n'f'i'g'.'j's'`' 'f'i'l'e',' 'e'n'a'b'l'e' '`'g'a't's'b'y'-'p'l'u'g'i'n'-'p'o's't'c's's'`'.' 'S'e'e' '['t'h'e' 'p'l'u'g'i'n'''s' 'd'o'c'u'm'e'n't'a't'i'o'n']'('h't't'p's':'/'/'w'w'w'.'g'a't's'b'y'j's'.'c'o'm'/'p'l'u'g'i'n's'/'g'a't's'b'y'-'p'l'u'g'i'n'-'p'o's't'c's's'/')' 'f'o'r' 'm'o'r'e' 'i'n'f'o'r'm'a't'i'o'n'.'

*gatsby-config.js*
```js
module.exports = {
          plugins: [
            // [!code highlight:2]
            'gatsby-plugin-postcss',
            // ...
          ],
        }
```

#### Step 4: Configure PostCSS Plugins

'C'r'e'a't'e' 'a' '`'p'o's't'c's's'.'c'o'n'f'i'g'.'j's'`' 'f'i'l'e' 'i'n' 't'h'e' 'r'o'o't' 'o'f' 'y'o'u'r' 'p'r'o'j'e'c't' 'a'n'd' 'a'd'd' 't'h'e' '`'@'t'a'i'l'w'i'n'd'c's's'/'p'o's't'c's's'`' 'p'l'u'g'i'n' 't'o' 'y'o'u'r' 'P'o's't'C'S'S' 'c'o'n'f'i'g'u'r'a't'i'o'n'.'

*postcss.config.js*
```js
module.exports = {
          plugins: {
            // [!code highlight:2]
            "@tailwindcss/postcss": {},
          },
        };
```

#### Step 5: Import Tailwind CSS

'C'r'e'a't'e' 'a' '`'.'/'s'r'c'/'s't'y'l'e's'/'g'l'o'b'a'l'.'c's's'`' 'f'i'l'e' 'a'n'd' 'a'd'd' 'a'n' '`'@'i'm'p'o'r't'`' 'f'o'r' 'T'a'i'l'w'i'n'd' 'C'S'S'.'

*global.css*
```css
@import "tailwindcss";
```

#### Step 6: Import the CSS file

'C'r'e'a't'e' 'a' '`'g'a't's'b'y'-'b'r'o'w's'e'r'.'j's'`' 'f'i'l'e' 'a't' 't'h'e' 'r'o'o't' 'o'f' 'y'o'u'r' 'p'r'o'j'e'c't' 'i'f' 'i't' 'd'o'e's'n'''t' 'a'l'r'e'a'd'y' 'e'x'i's't',' 'a'n'd' 'i'm'p'o'r't' 'y'o'u'r' 'n'e'w'l'y'-'c'r'e'a't'e'd' '`'.'/'s'r'c'/'s't'y'l'e's'/'g'l'o'b'a'l'.'c's's'`' 'f'i'l'e'.'

*gatsby-browser.js*
```js
import './src/styles/global.css';
```

#### Step 7: Start your build process

'R'u'n' 'y'o'u'r' 'b'u'i'l'd' 'p'r'o'c'e's's' 'w'i't'h' '`'g'a't's'b'y' 'd'e'v'e'l'o'p'`'.'

*Terminal*
```shell
gatsby develop
```

#### Step 8: Start using Tailwind in your project

'S't'a'r't' 'u's'i'n'g' 'T'a'i'l'w'i'n'd'''s' 'u't'i'l'i't'y' 'c'l'a's's'e's' 't'o' 's't'y'l'e' 'y'o'u'r' 'c'o'n't'e'n't'.'

*index.js*
```js
export default function IndexPage() {
          return (
            <Layout>
              /* [!code highlight:4] */
              <h1 className="text-3xl font-bold underline">
                Hello world!
              </h1>
            </Layout>
          )
        }
```

---

### <a id="laravel"></a>Install Tailwind CSS with Laravel

Setting up Tailwind CSS in a Laravel project.

#### Step 1: Create your project

'S't'a'r't' 'b'y' 'c'r'e'a't'i'n'g' 'a' 'n'e'w' 'L'a'r'a'v'e'l' 'p'r'o'j'e'c't' 'i'f' 'y'o'u' 'd'o'n'''t' 'h'a'v'e' 'o'n'e' 's'e't' 'u'p' 'a'l'r'e'a'd'y'.' 'T'h'e' 'm'o's't' 'c'o'm'm'o'n' 'a'p'p'r'o'a'c'h' 'i's' 't'o' 'u's'e' '['t'h'e' 'L'a'r'a'v'e'l' 'i'n's't'a'l'l'e'r']'('h't't'p's':'/'/'l'a'r'a'v'e'l'.'c'o'm'/'d'o'c's'#'c'r'e'a't'i'n'g'-'a'n'-'a'p'p'l'i'c'a't'i'o'n')'.'

*Terminal*
```shell
laravel new my-project
        cd my-project
```

#### Step 2: Install Tailwind CSS

'I'n's't'a'l'l' '`'@'t'a'i'l'w'i'n'd'c's's'/'v'i't'e'`' 'a'n'd' 'i't's' 'p'e'e'r' 'd'e'p'e'n'd'e'n'c'i'e's' 'v'i'a' 'n'p'm'.'

*Terminal*
```shell
npm install tailwindcss @tailwindcss/vite
```

#### Step 3: Install Tailwind CSS

'I'n's't'a'l'l' '`'@'t'a'i'l'w'i'n'd'c's's'/'p'o's't'c's's'`' 'a'n'd' 'i't's' 'p'e'e'r' 'd'e'p'e'n'd'e'n'c'i'e's' 'v'i'a' 'n'p'm'.'

*Terminal*
```shell
npm install tailwindcss @tailwindcss/postcss postcss
```

#### Step 4: Configure Vite Plugin

'A'd'd' 't'h'e' '`'@'t'a'i'l'w'i'n'd'c's's'/'v'i't'e'`' 'p'l'u'g'i'n' 't'o' 'y'o'u'r' 'V'i't'e' 'c'o'n'f'i'g'u'r'a't'i'o'n'.'

*vite.config.ts*
```ts
import { defineConfig } from 'vite'
        // [!code highlight:2]
        import tailwindcss from '@tailwindcss/vite'

        export default defineConfig({
          plugins: [
            // [!code highlight:2]
            tailwindcss(),
            // …
          ],
        })
```

#### Step 5: Add Tailwind to your Laravel Mix configuration

'I'n' 'y'o'u'r' '`'w'e'b'p'a'c'k'.'m'i'x'.'j's'`' 'f'i'l'e',' 'a'd'd' '`'t'a'i'l'w'i'n'd'c's's'`' 'a's' 'a' 'P'o's't'C'S'S' 'p'l'u'g'i'n'.'

*webpack.mix.js*
```js
mix
          .js("resources/js/app.js", "public/js")
          .postCss("resources/css/app.css", "public/css", [
            // [!code highlight:2]
            require("@tailwindcss/postcss"),
          ]);
```

#### Step 6: Import Tailwind CSS

'A'd'd' 'a'n' '`'@'i'm'p'o'r't'`' 't'o' '`'.'/'r'e's'o'u'r'c'e's'/'c's's'/'a'p'p'.'c's's'`' 't'h'a't' 'i'm'p'o'r't's' 'T'a'i'l'w'i'n'd' 'C'S'S'.' 'A'd'd'i't'i'o'n'a'l'l'y',' 't'e'l'l' 'T'a'i'l'w'i'n'd' 'C'S'S' 't'o' 's'c'a'n' 's'o'm'e' 'd'i'r'e'c't'o'r'i'e's' 'f'o'r' 'u't'i'l'i't'i'e's'.'

*app.css*
```css
@import "tailwindcss";

        @source "../../vendor/laravel/framework/src/Illuminate/Pagination/resources/views/*.blade.php";
        @source "../../storage/framework/views/*.php";
        @source "../**/*.blade.php";
        @source "../**/*.js";
```

#### Step 7: Start your build process

'R'u'n' 'y'o'u'r' 'b'u'i'l'd' 'p'r'o'c'e's's' 'w'i't'h' '`'n'p'm' 'r'u'n' 'd'e'v'`'.'

*Terminal*
```shell
npm run dev
```

#### Step 8: Start your build process

'R'u'n' 'y'o'u'r' 'b'u'i'l'd' 'p'r'o'c'e's's' 'w'i't'h' '`'n'p'm' 'r'u'n' 'w'a't'c'h'`'.'

*Terminal*
```shell
npm run watch
```

#### Step 9: Start using Tailwind in your project

'M'a'k'e' 's'u'r'e' 'y'o'u'r' 'c'o'm'p'i'l'e'd' 'C'S'S' 'i's' 'i'n'c'l'u'd'e'd' 'i'n' 't'h'e' '`'<'h'e'a'd'>'`' 't'h'e'n' 's't'a'r't' 'u's'i'n'g' 'T'a'i'l'w'i'n'd'''s' 'u't'i'l'i't'y' 'c'l'a's's'e's' 't'o' 's't'y'l'e' 'y'o'u'r' 'c'o'n't'e'n't'.'

*app.blade.php*
```blade
<!doctype html>
        <html>
          <head>
            <meta charset="utf-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <!-- [!code highlight:2] -->
            @vite('resources/css/app.css')
          </head>
          <body>
            <!-- [!code highlight:4] -->
            <h1 class="text-3xl font-bold underline">
              <!-- prettier-ignore -->
              Hello world!
            </h1>
          </body>
        </html>
```

#### Step 10: Start using Tailwind in your project

'M'a'k'e' 's'u'r'e' 'y'o'u'r' 'c'o'm'p'i'l'e'd' 'C'S'S' 'i's' 'i'n'c'l'u'd'e'd' 'i'n' 't'h'e' '`'<'h'e'a'd'>'`' 't'h'e'n' 's't'a'r't' 'u's'i'n'g' 'T'a'i'l'w'i'n'd'''s' 'u't'i'l'i't'y' 'c'l'a's's'e's' 't'o' 's't'y'l'e' 'y'o'u'r' 'c'o'n't'e'n't'.'

*app.blade.php*
```blade
<!doctype html>
        <html>
          <head>
            <meta charset="utf-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <!-- [!code highlight:2] -->
            <link href="{{ asset('css/app.css') }}" rel="stylesheet" />
          </head>
          <body>
            <!-- [!code highlight:4] -->
            <h1 class="text-3xl font-bold underline">
              <!-- prettier-ignore -->
              Hello world!
            </h1>
          </body>
        </html>
```

---

### <a id="meteor"></a>Install Tailwind CSS with Meteor

Setting up Tailwind CSS in a Meteor project.

#### Step 1: Create your project

'S't'a'r't' 'b'y' 'c'r'e'a't'i'n'g' 'a' 'n'e'w' 'M'e't'e'o'r' 'p'r'o'j'e'c't' 'i'f' 'y'o'u' 'd'o'n'''t' 'h'a'v'e' 'o'n'e' 's'e't' 'u'p' 'a'l'r'e'a'd'y'.' 'T'h'e' 'm'o's't' 'c'o'm'm'o'n' 'a'p'p'r'o'a'c'h' 'i's' 't'o' 'u's'e' '['t'h'e' 'M'e't'e'o'r' 'C'L'I']'('h't't'p's':'/'/'d'o'c's'.'m'e't'e'o'r'.'c'o'm'/'a'b'o'u't'/'i'n's't'a'l'l'.'h't'm'l')'.'

*Terminal*
```shell
npx meteor create my-project
        cd my-project
```

#### Step 2: Install Tailwind CSS

'I'n's't'a'l'l' '`'@'t'a'i'l'w'i'n'd'c's's'/'p'o's't'c's's'`' 'a'n'd' 'i't's' 'p'e'e'r' 'd'e'p'e'n'd'e'n'c'i'e's' 'v'i'a' 'n'p'm'.'

*Terminal*
```shell
npm install tailwindcss @tailwindcss/postcss postcss postcss-load-config
```

#### Step 3: Configure PostCSS Plugins

'C'r'e'a't'e' 'a' '`'p'o's't'c's's'.'c'o'n'f'i'g'.'m'j's'`' 'f'i'l'e' 'i'n' 't'h'e' 'r'o'o't' 'o'f' 'y'o'u'r' 'p'r'o'j'e'c't' 'a'n'd' 'a'd'd' 't'h'e' '`'@'t'a'i'l'w'i'n'd'c's's'/'p'o's't'c's's'`' 'p'l'u'g'i'n' 't'o' 'y'o'u'r' 'P'o's't'C'S'S' 'c'o'n'f'i'g'u'r'a't'i'o'n'.'

*postcss.config.mjs*
```js
export default {
          plugins: {
            // [!code highlight:2]
            "@tailwindcss/postcss": {},
          },
        };
```

#### Step 4: Import Tailwind CSS

'A'd'd' 'a'n' '`'@'i'm'p'o'r't'`' 'f'o'r' 'T'a'i'l'w'i'n'd' 'C'S'S' 't'o' 'y'o'u'r' '`'.'/'c'l'i'e'n't'/'m'a'i'n'.'c's's'`' 'f'i'l'e'.'

*main.css*
```css
@import "tailwindcss";
```

#### Step 5: Start your build process

'R'u'n' 'y'o'u'r' 'b'u'i'l'd' 'p'r'o'c'e's's' 'w'i't'h' '`'n'p'm' 'r'u'n' 's't'a'r't'`'.'

*Terminal*
```shell
npm run start
```

#### Step 6: Start using Tailwind in your project

'S't'a'r't' 'u's'i'n'g' 'T'a'i'l'w'i'n'd'''s' 'u't'i'l'i't'y' 'c'l'a's's'e's' 't'o' 's't'y'l'e' 'y'o'u'r' 'c'o'n't'e'n't'.'

*App.jsx*
```jsx
export const App = () => (
          // [!code highlight:4]
          <h1 className="text-3xl font-bold underline">
            Hello world!
          </h1>
        )
```

---

### <a id="nextjs"></a>Install Tailwind CSS with Next.js

Setting up Tailwind CSS in a Next.js project.

#### Step 1: Create your project

'S't'a'r't' 'b'y' 'c'r'e'a't'i'n'g' 'a' 'n'e'w' 'N'e'x't'.'j's' 'p'r'o'j'e'c't' 'i'f' 'y'o'u' 'd'o'n'''t' 'h'a'v'e' 'o'n'e' 's'e't' 'u'p' 'a'l'r'e'a'd'y'.' 'T'h'e' 'm'o's't' 'c'o'm'm'o'n' 'a'p'p'r'o'a'c'h' 'i's' 't'o' 'u's'e' '['C'r'e'a't'e' 'N'e'x't' 'A'p'p']'('h't't'p's':'/'/'n'e'x't'j's'.'o'r'g'/'d'o'c's'/'a'p'i'-'r'e'f'e'r'e'n'c'e'/'c'r'e'a't'e'-'n'e'x't'-'a'p'p')'.'

*Terminal*
```shell
npx create-next-app@latest my-project --typescript --eslint --app
        cd my-project
```

#### Step 2: Install Tailwind CSS

'I'n's't'a'l'l' '`'@'t'a'i'l'w'i'n'd'c's's'/'p'o's't'c's's'`' 'a'n'd' 'i't's' 'p'e'e'r' 'd'e'p'e'n'd'e'n'c'i'e's' 'v'i'a' 'n'p'm'.'

*Terminal*
```shell
npm install tailwindcss @tailwindcss/postcss postcss
```

#### Step 3: Configure PostCSS Plugins

'C'r'e'a't'e' 'a' '`'p'o's't'c's's'.'c'o'n'f'i'g'.'m'j's'`' 'f'i'l'e' 'i'n' 't'h'e' 'r'o'o't' 'o'f' 'y'o'u'r' 'p'r'o'j'e'c't' 'a'n'd' 'a'd'd' 't'h'e' '`'@'t'a'i'l'w'i'n'd'c's's'/'p'o's't'c's's'`' 'p'l'u'g'i'n' 't'o' 'y'o'u'r' 'P'o's't'C'S'S' 'c'o'n'f'i'g'u'r'a't'i'o'n'.'

*postcss.config.mjs*
```js
const config = {
          plugins: {
            // [!code highlight:2]
            "@tailwindcss/postcss": {},
          },
        };

        export default config;
```

#### Step 4: Import Tailwind CSS

'A'd'd' 'a'n' '`'@'i'm'p'o'r't'`' 't'o' '`'.'/'a'p'p'/'g'l'o'b'a'l's'.'c's's'`' 't'h'a't' 'i'm'p'o'r't's' 'T'a'i'l'w'i'n'd' 'C'S'S'.'

*globals.css*
```css
@import "tailwindcss";
```

#### Step 5: Start your build process

'R'u'n' 'y'o'u'r' 'b'u'i'l'd' 'p'r'o'c'e's's' 'w'i't'h' '`'n'p'm' 'r'u'n' 'd'e'v'`'.'

*Terminal*
```shell
npm run dev
```

#### Step 6: Start using Tailwind in your project

'S't'a'r't' 'u's'i'n'g' 'T'a'i'l'w'i'n'd'''s' 'u't'i'l'i't'y' 'c'l'a's's'e's' 't'o' 's't'y'l'e' 'y'o'u'r' 'c'o'n't'e'n't'.'

*page.tsx*
```jsx
export default function Home() {
          return (
            // [!code highlight:4]
            <h1 className="text-3xl font-bold underline">
              Hello world!
            </h1>
          )
        }
```

---

### <a id="nuxtjs"></a>Install Tailwind CSS with Nuxt

Setting up Tailwind CSS in a Nuxt project.

#### Step 1: Create your project

'S't'a'r't' 'b'y' 'c'r'e'a't'i'n'g' 'a' 'n'e'w' 'N'u'x't' 'p'r'o'j'e'c't' 'i'f' 'y'o'u' 'd'o'n'''t' 'h'a'v'e' 'o'n'e' 's'e't' 'u'p' 'a'l'r'e'a'd'y'.' 'T'h'e' 'm'o's't' 'c'o'm'm'o'n' 'a'p'p'r'o'a'c'h' 'i's' 't'o' 'u's'e' '['C'r'e'a't'e' 'N'u'x't']'('h't't'p's':'/'/'n'u'x't'.'c'o'm'/'d'o'c's'/'4'.'x'/'g'e't't'i'n'g'-'s't'a'r't'e'd'/'i'n's't'a'l'l'a't'i'o'n'#'n'e'w'-'p'r'o'j'e'c't')'.'

*Terminal*
```shell
npm create nuxt my-project
        cd my-project
```

#### Step 2: Install Tailwind CSS

'I'n's't'a'l'l' '`'@'t'a'i'l'w'i'n'd'c's's'/'v'i't'e'`' 'a'n'd' 'i't's' 'p'e'e'r' 'd'e'p'e'n'd'e'n'c'i'e's' 'v'i'a' 'n'p'm'.'

*Terminal*
```shell
npm install tailwindcss @tailwindcss/vite
```

#### Step 3: Configure Vite Plugin

'A'd'd' 't'h'e' '`'@'t'a'i'l'w'i'n'd'c's's'/'v'i't'e'`' 'p'l'u'g'i'n' 't'o' 'y'o'u'r' 'N'u'x't' 'c'o'n'f'i'g'u'r'a't'i'o'n' 'a's' 'a' 'V'i't'e' 'p'l'u'g'i'n'.'

*nuxt.config.ts*
```ts
// [!code highlight:2]
        import tailwindcss from "@tailwindcss/vite";

        export default defineNuxtConfig({
          compatibilityDate: "2025-07-15",
          devtools: { enabled: true },
          vite: {
            plugins: [
              // [!code highlight:2]
              tailwindcss(),
            ],
          },
        });
```

#### Step 4: Import Tailwind CSS

'C'r'e'a't'e' 'a'n' '`'.'/'a'p'p'/'a's's'e't's'/'c's's'/'m'a'i'n'.'c's's'`' 'f'i'l'e' 'a'n'd' 'a'd'd' 'a'n' '`'@'i'm'p'o'r't'`' 't'h'a't' 'i'm'p'o'r't's' 'T'a'i'l'w'i'n'd' 'C'S'S'.'

*main.css*
```css
@import "tailwindcss";
```

#### Step 5: Add the CSS file globally

'A'd'd' 'y'o'u'r' 'n'e'w'l'y'-'c'r'e'a't'e'd' '`'.'/'a'p'p'/'a's's'e't's'/'c's's'/'m'a'i'n'.'c's's'`' 't'o' 't'h'e' '`'c's's'`' 'a'r'r'a'y' 'i'n' 'y'o'u'r' '`'n'u'x't'.'c'o'n'f'i'g'.'t's'`' 'f'i'l'e'.'

*nuxt.config.ts*
```ts
import tailwindcss from "@tailwindcss/vite";

        export default defineNuxtConfig({
          compatibilityDate: "2025-07-15",
          devtools: { enabled: true },
          // [!code highlight:2]
          css: ['./app/assets/css/main.css'],
          vite: {
            plugins: [
              tailwindcss(),
            ],
          },
        });
```

#### Step 6: Start your build process

'R'u'n' 'y'o'u'r' 'b'u'i'l'd' 'p'r'o'c'e's's' 'w'i't'h' '`'n'p'm' 'r'u'n' 'd'e'v'`'.'

*Terminal*
```shell
npm run dev
```

#### Step 7: Start using Tailwind in your project

'S't'a'r't' 'u's'i'n'g' 'T'a'i'l'w'i'n'd'''s' 'u't'i'l'i't'y' 'c'l'a's's'e's' 't'o' 's't'y'l'e' 'y'o'u'r' 'c'o'n't'e'n't'.'

*app.vue*
```vue
<template>
          <!-- [!code highlight:4] -->
          <h1 class="text-3xl font-bold underline">
            <!-- prettier-ignore -->
            Hello world!
          </h1>
        </template>
```

---

### <a id="parcel"></a>Install Tailwind CSS with Parcel

Setting up Tailwind CSS in a Parcel project.

#### Step 1: Create your project

'S't'a'r't' 'b'y' 'c'r'e'a't'i'n'g' 'a' 'n'e'w' 'P'a'r'c'e'l' 'p'r'o'j'e'c't' 'i'f' 'y'o'u' 'd'o'n'''t' 'h'a'v'e' 'o'n'e' 's'e't' 'u'p' 'a'l'r'e'a'd'y'.' 'T'h'e' 'm'o's't' 'c'o'm'm'o'n' 'a'p'p'r'o'a'c'h' 'i's' 't'o' 'a'd'd' 'P'a'r'c'e'l' 'a's' 'a' 'd'e'v'-'d'e'p'e'n'd'e'n'c'y' 't'o' 'y'o'u'r' 'p'r'o'j'e'c't' 'a's' 'o'u't'l'i'n'e'd' 'i'n' 't'h'e'i'r' '['g'e't't'i'n'g' 's't'a'r't'e'd' 'g'u'i'd'e']'('h't't'p's':'/'/'p'a'r'c'e'l'j's'.'o'r'g'/'g'e't't'i'n'g'-'s't'a'r't'e'd'/'w'e'b'a'p'p'/')'.'

*Terminal*
```shell
mkdir my-project
        cd my-project
        npm init -y
        npm install parcel
        mkdir src
        touch src/index.html
```

#### Step 2: Install Tailwind CSS

'I'n's't'a'l'l' '`'@'t'a'i'l'w'i'n'd'c's's'/'p'o's't'c's's'`' 'a'n'd' 'i't's' 'p'e'e'r' 'd'e'p'e'n'd'e'n'c'i'e's' 'v'i'a' 'n'p'm'.'

*Terminal*
```shell
npm install tailwindcss @tailwindcss/postcss
```

#### Step 3: Configure PostCSS

'C'r'e'a't'e' 'a' '`'.'p'o's't'c's's'r'c'`' 'f'i'l'e' 'i'n' 'y'o'u'r' 'p'r'o'j'e'c't' 'r'o'o't',' 'a'n'd' 'e'n'a'b'l'e' 't'h'e' '`'@'t'a'i'l'w'i'n'd'c's's'/'p'o's't'c's's'`' 'p'l'u'g'i'n'.'

*.postcssrc*
```json
{
          "plugins": {
            "@tailwindcss/postcss": {}
          }
        }
```

#### Step 4: Import Tailwind CSS

'C'r'e'a't'e' 'a' '`'.'/'s'r'c'/'i'n'd'e'x'.'c's's'`' 'f'i'l'e' 'a'n'd' 'a'd'd' 'a'n' '`'@'i'm'p'o'r't'`' 'f'o'r' 'T'a'i'l'w'i'n'd' 'C'S'S'.'

*index.css*
```css
@import "tailwindcss";
```

#### Step 5: Start your build process

'R'u'n' 'y'o'u'r' 'b'u'i'l'd' 'p'r'o'c'e's's' 'w'i't'h' '`'n'p'x' 'p'a'r'c'e'l' 's'r'c'/'i'n'd'e'x'.'h't'm'l'`'.'

*Terminal*
```shell
npx parcel src/index.html
```

#### Step 6: Start using Tailwind in your project

'A'd'd' 'y'o'u'r' 'C'S'S' 'f'i'l'e' 't'o' 't'h'e' '`'<'h'e'a'd'>'`' 'a'n'd' 's't'a'r't' 'u's'i'n'g' 'T'a'i'l'w'i'n'd'''s' 'u't'i'l'i't'y' 'c'l'a's's'e's' 't'o' 's't'y'l'e' 'y'o'u'r' 'c'o'n't'e'n't'.'

*index.html*
```html
<!doctype html>
        <html>
          <head>
            <meta charset="UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <!-- [!code highlight:2] -->
            <link href="./index.css" type="text/css" rel="stylesheet" />
          </head>
          <body>
            <!-- [!code highlight:4] -->
            <h1 class="text-3xl font-bold underline">
              <!-- prettier-ignore -->
              Hello world!
            </h1>
          </body>
        </html>
```

---

### <a id="phoenix"></a>Install Tailwind CSS with Phoenix

Setting up Tailwind CSS in a Phoenix project.

#### Step 1: Create your project

'S't'a'r't' 'b'y' 'c'r'e'a't'i'n'g' 'a' 'n'e'w' 'P'h'o'e'n'i'x' 'p'r'o'j'e'c't' 'i'f' 'y'o'u' 'd'o'n'''t' 'h'a'v'e' 'o'n'e' 's'e't' 'u'p' 'a'l'r'e'a'd'y'.' 'Y'o'u' 'c'a'n' 'f'o'l'l'o'w' 't'h'e'i'r' '['i'n's't'a'l'l'a't'i'o'n' 'g'u'i'd'e']'('h't't'p's':'/'/'h'e'x'd'o'c's'.'p'm'/'p'h'o'e'n'i'x'/'i'n's't'a'l'l'a't'i'o'n'.'h't'm'l')' 't'o' 'g'e't' 'u'p' 'a'n'd' 'r'u'n'n'i'n'g'.'

*Terminal*
```shell
mix phx.new myproject
        cd myproject
```

#### Step 2: Install the Tailwind plugin

'A'd'd' 't'h'e' 'T'a'i'l'w'i'n'd' 'p'l'u'g'i'n' 't'o' 'y'o'u'r' 'd'e'p'e'n'd'e'n'c'i'e's' 'a'n'd' 'r'u'n' '`'m'i'x' 'd'e'p's'.'g'e't'`' 't'o' 'i'n's't'a'l'l' 'i't'.'

#### Step 3: Configure the Tailwind plugin

'I'n' 'y'o'u'r' '`'c'o'n'f'i'g'/'c'o'n'f'i'g'.'e'x's'`' 'f'i'l'e' 'y'o'u' 'c'a'n' 's'e't' 'w'h'i'c'h' 'v'e'r's'i'o'n' 'o'f' 'T'a'i'l'w'i'n'd' 'C'S'S' 'y'o'u' 'w'a'n't' 't'o' 'u's'e' 'a'n'd' 'c'u's't'o'm'i'z'e' 'y'o'u'r' 'a's's'e't' 'p'a't'h's'.'

#### Step 4: Update your deployment script

'C'o'n'f'i'g'u'r'e' 'y'o'u'r' '`'a's's'e't's'.'d'e'p'l'o'y'`' 'a'l'i'a's' 't'o' 'b'u'i'l'd' 'y'o'u'r' 'C'S'S' 'o'n' 'd'e'p'l'o'y'm'e'n't'.'

#### Step 5: Enable watcher in development

'A'd'd' 'T'a'i'l'w'i'n'd' 't'o' 'y'o'u'r' 'l'i's't' 'o'f' 'w'a't'c'h'e'r's' 'i'n' 'y'o'u'r' '`'.'/'c'o'n'f'i'g'/'d'e'v'.'e'x's'`' 'f'i'l'e'.'

#### Step 6: Install Tailwind CSS

'R'u'n' 't'h'e' 'i'n's't'a'l'l' 'c'o'm'm'a'n'd' 't'o' 'd'o'w'n'l'o'a'd' 't'h'e' 's't'a'n'd'a'l'o'n'e' 'T'a'i'l'w'i'n'd' 'C'L'I'.'

*Terminal*
```shell
mix tailwind.install
```

#### Step 7: Import Tailwind CSS

'A'd'd' 'a'n' '`'@'i'm'p'o'r't'`' 't'o' '`'.'/'a's's'e't's'/'c's's'/'a'p'p'.'c's's'`' 't'h'a't' 'i'm'p'o'r't's' 'T'a'i'l'w'i'n'd' 'C'S'S'.'

*app.css*
```css
@import "tailwindcss";
```

#### Step 8: Remove the default CSS import

'R'e'm'o'v'e' 't'h'e' 'C'S'S' 'i'm'p'o'r't' 'f'r'o'm' '`'.'/'a's's'e't's'/'j's'/'a'p'p'.'j's'`',' 'a's' 'T'a'i'l'w'i'n'd' 'i's' 'n'o'w' 'h'a'n'd'l'i'n'g' 't'h'i's' 'f'o'r' 'y'o'u'.'

*app.js*
```js
// [!code --:3]
        // Remove this line if you add your own CSS build pipeline (e.g postcss).
        import "../css/app.css"
```

#### Step 9: Start your build process

'R'u'n' 'y'o'u'r' 'b'u'i'l'd' 'p'r'o'c'e's's' 'w'i't'h' '`'m'i'x' 'p'h'x'.'s'e'r'v'e'r'`'.'

*Terminal*
```shell
mix phx.server
```

#### Step 10: Start using Tailwind in your project

'S't'a'r't' 'u's'i'n'g' 'T'a'i'l'w'i'n'd'''s' 'u't'i'l'i't'y' 'c'l'a's's'e's' 't'o' 's't'y'l'e' 'y'o'u'r' 'c'o'n't'e'n't'.'

*index.html.heex*
```html
<!-- [!code highlight:4] -->
        <h1 class="text-3xl font-bold underline">
          <!-- prettier-ignore -->
          Hello world!
        </h1>
```

---

### <a id="qwik"></a>Install Tailwind CSS with Qwik

Setting up Tailwind CSS in an Qwik project.

#### Step 1: Create your project

'S't'a'r't' 'b'y' 'c'r'e'a't'i'n'g' 'a' 'n'e'w' 'Q'w'i'k' 'p'r'o'j'e'c't' 'i'f' 'y'o'u' 'd'o'n'''t' 'h'a'v'e' 'o'n'e' 's'e't' 'u'p' 'a'l'r'e'a'd'y'.' 'T'h'e' 'm'o's't' 'c'o'm'm'o'n' 'a'p'p'r'o'a'c'h' 'i's' 't'o' 'u's'e' '['C'r'e'a't'e' 'Q'w'i'k']'('h't't'p's':'/'/'q'w'i'k'.'d'e'v'/'d'o'c's'/'g'e't't'i'n'g'-'s't'a'r't'e'd'/'#'c'r'e'a't'e'-'a'n'-'a'p'p'-'u's'i'n'g'-'t'h'e'-'c'l'i')'.'

*Terminal*
```shell
npm create qwik@latest empty my-project
        cd my-project
```

#### Step 2: Install Tailwind CSS

'I'n's't'a'l'l' '`'@'t'a'i'l'w'i'n'd'c's's'/'v'i't'e'`' 'a'n'd' 'i't's' 'p'e'e'r' 'd'e'p'e'n'd'e'n'c'i'e's' 'v'i'a' 'n'p'm'.'

*Terminal*
```shell
npm install tailwindcss @tailwindcss/vite
```

#### Step 3: Configure Vite Plugin

'A'd'd' 't'h'e' '`'@'t'a'i'l'w'i'n'd'c's's'/'v'i't'e'`' 'p'l'u'g'i'n' 't'o' 'y'o'u'r' 'V'i't'e' 'c'o'n'f'i'g'u'r'a't'i'o'n'.'

*vite.config.ts*
```ts
import { defineConfig } from 'vite'
        import { qwikVite } from "@builder.io/qwik/optimizer";
        import { qwikCity } from "@builder.io/qwik-city/vite";
        // …

        // [!code highlight:2]
        import tailwindcss from '@tailwindcss/vite'

        export default defineConfig(({ command, mode }): UserConfig => {
          return {
            plugins: [
              // [!code highlight:2]
              tailwindcss(),
              qwikCity(),
              qwikVite(),
              tsconfigPaths(),
            ],

            // …
          }
        })
```

#### Step 4: Import Tailwind CSS

'A'd'd' 'a'n' '`'@'i'm'p'o'r't'`' 't'o' '`'.'/'s'r'c'/'g'l'o'b'a'l'.'c's's'`' 't'h'a't' 'i'm'p'o'r't's' 'T'a'i'l'w'i'n'd' 'C'S'S'.'

*global.css*
```css
@import "tailwindcss";
```

#### Step 5: Start your build process

'R'u'n' 'y'o'u'r' 'b'u'i'l'd' 'p'r'o'c'e's's' 'w'i't'h' '`'n'p'm' 'r'u'n' 'd'e'v'`'.'

*Terminal*
```shell
npm run dev
```

#### Step 6: Start using Tailwind in your project

'S't'a'r't' 'u's'i'n'g' 'T'a'i'l'w'i'n'd'''s' 'u't'i'l'i't'y' 'c'l'a's's'e's' 't'o' 's't'y'l'e' 'y'o'u'r' 'c'o'n't'e'n't'.'

*index.tsx*
```tsx
import { component$ } from '@builder.io/qwik'

        export default component$(() => {
          return (
            // [!code highlight:4]
            <h1 class="text-3xl font-bold underline">
              Hello World!
            </h1>
          )
        })
```

---

### <a id="react-router"></a>Install Tailwind CSS with React Router

Setting up Tailwind CSS in a React Router project.

#### Step 1: Create your project

'S't'a'r't' 'b'y' 'c'r'e'a't'i'n'g' 'a' 'n'e'w' 'R'e'a'c't' 'R'o'u't'e'r' 'p'r'o'j'e'c't' 'i'f' 'y'o'u' 'd'o'n'''t' 'h'a'v'e' 'o'n'e' 's'e't' 'u'p' 'a'l'r'e'a'd'y'.' 'T'h'e' 'm'o's't' 'c'o'm'm'o'n' 'a'p'p'r'o'a'c'h' 'i's' 't'o' 'u's'e' '['C'r'e'a't'e' 'R'e'a'c't' 'R'o'u't'e'r']'('h't't'p's':'/'/'r'e'a'c't'r'o'u't'e'r'.'c'o'm'/'s't'a'r't'/'f'r'a'm'e'w'o'r'k'/'i'n's't'a'l'l'a't'i'o'n')'.'

*Terminal*
```shell
npx create-react-router@latest my-project
        cd my-project
```

#### Step 2: Install Tailwind CSS

'I'n's't'a'l'l' '`'@'t'a'i'l'w'i'n'd'c's's'/'v'i't'e'`' 'a'n'd' 'i't's' 'p'e'e'r' 'd'e'p'e'n'd'e'n'c'i'e's' 'v'i'a' 'n'p'm'.'

*Terminal*
```shell
npm install tailwindcss @tailwindcss/vite
```

#### Step 3: Configure Vite Plugin

'A'd'd' 't'h'e' '`'@'t'a'i'l'w'i'n'd'c's's'/'v'i't'e'`' 'p'l'u'g'i'n' 't'o' 'y'o'u'r' 'V'i't'e' 'c'o'n'f'i'g'u'r'a't'i'o'n'.'

*vite.config.ts*
```ts
import { reactRouter } from "@react-router/dev/vite";
        import { defineConfig } from "vite";
        import tsconfigPaths from "vite-tsconfig-paths";
        // [!code highlight:2]
        import tailwindcss from "@tailwindcss/vite";

        export default defineConfig({
          plugins: [
            // [!code highlight:2]
            tailwindcss(),
            reactRouter(),
            tsconfigPaths(),
          ],
        });
```

#### Step 4: Import Tailwind CSS

'A'd'd' 'a'n' '`'@'i'm'p'o'r't'`' 't'o' '`'.'/'a'p'p'/'a'p'p'.'c's's'`' 't'h'a't' 'i'm'p'o'r't's' 'T'a'i'l'w'i'n'd' 'C'S'S'.'

*app.css*
```css
@import "tailwindcss";
```

#### Step 5: Start your build process

'R'u'n' 'y'o'u'r' 'b'u'i'l'd' 'p'r'o'c'e's's' 'w'i't'h' '`'n'p'm' 'r'u'n' 'd'e'v'`'.'

*Terminal*
```shell
npm run dev
```

#### Step 6: Start using Tailwind in your project

'S't'a'r't' 'u's'i'n'g' 'T'a'i'l'w'i'n'd'''s' 'u't'i'l'i't'y' 'c'l'a's's'e's' 't'o' 's't'y'l'e' 'y'o'u'r' 'c'o'n't'e'n't'.'

*home.tsx*
```tsx
export default function Home() {
          return (
            // [!code highlight:4]
            <h1 className="text-3xl font-bold underline">
              Hello world!
            </h1>
          )
        }
```

---

### <a id="rspack"></a>Install Tailwind CSS with Rspack

Setting up Tailwind CSS in a Rspack project.

#### Step 1: Create your project

'S't'a'r't' 'b'y' 'c'r'e'a't'i'n'g' 'a' 'n'e'w' 'R's'p'a'c'k' 'p'r'o'j'e'c't' 'i'f' 'y'o'u' 'd'o'n'''t' 'h'a'v'e' 'o'n'e' 's'e't' 'u'p' 'a'l'r'e'a'd'y'.' 'T'h'e' 'm'o's't' 'c'o'm'm'o'n' 'a'p'p'r'o'a'c'h' 'i's' 't'o' 'u's'e' '['R's'p'a'c'k' 'C'L'I']'('h't't'p's':'/'/'r's'p'a'c'k'.'d'e'v'/'g'u'i'd'e'/'s't'a'r't'/'q'u'i'c'k'-'s't'a'r't'#'u's'i'n'g'-'t'h'e'-'r's'p'a'c'k'-'c'l'i')'.'

*Terminal*
```shell
npm create rspack@latest
```

#### Step 2: Install Tailwind CSS

'I'n's't'a'l'l' '`'@'t'a'i'l'w'i'n'd'c's's'/'p'o's't'c's's'`' 'a'n'd' 'i't's' 'p'e'e'r' 'd'e'p'e'n'd'e'n'c'i'e's'.'

*Terminal*
```shell
npm install tailwindcss @tailwindcss/postcss postcss postcss-loader
```

#### Step 3: Enable PostCSS support

'I'n' 'y'o'u'r' '`'r's'p'a'c'k'.'c'o'n'f'i'g'.'j's'`' 'f'i'l'e',' 'e'n'a'b'l'e' 't'h'e' 'P'o's't'C'S'S' 'l'o'a'd'e'r'.' 'S'e'e' '['t'h'e' 'd'o'c'u'm'e'n't'a't'i'o'n']'('h't't'p's':'/'/'r's'p'a'c'k'.'d'e'v'/'g'u'i'd'e'/'t'e'c'h'/'c's's'#'t'a'i'l'w'i'n'd'-'c's's')' 'f'o'r' 'm'o'r'e' 'i'n'f'o'r'm'a't'i'o'n'.'

*rspack.config.ts*
```ts
export default defineConfig({
          // ...
          module: {
            rules: [
              // [!code highlight:6]
              {
                test: /\.css$/,
                use: ["postcss-loader"],
                type: "css",
              },
              // ...
            ],
          },
        }
```

#### Step 4: Configure PostCSS Plugins

'C'r'e'a't'e' 'a' '`'p'o's't'c's's'.'c'o'n'f'i'g'.'m'j's'`' 'f'i'l'e' 'i'n' 't'h'e' 'r'o'o't' 'o'f' 'y'o'u'r' 'p'r'o'j'e'c't' 'a'n'd' 'a'd'd' 't'h'e' '`'@'t'a'i'l'w'i'n'd'c's's'/'p'o's't'c's's'`' 'p'l'u'g'i'n' 't'o' 'y'o'u'r' 'P'o's't'C'S'S' 'c'o'n'f'i'g'u'r'a't'i'o'n'.'

*postcss.config.mjs*
```js
export default {
          plugins: {
            // [!code highlight:2]
            "@tailwindcss/postcss": {},
          },
        };
```

#### Step 5: Import Tailwind CSS

'A'd'd' 'a'n' '`'@'i'm'p'o'r't'`' 't'o' '`'.'/'s'r'c'/'i'n'd'e'x'.'c's's'`' 't'h'a't' 'i'm'p'o'r't's' 'T'a'i'l'w'i'n'd' 'C'S'S'.'

*index.css*
```css
@import "tailwindcss";
```

#### Step 6: Import Tailwind CSS

'A'd'd' 'a'n' '`'@'i'm'p'o'r't'`' 't'o' '`'.'/'s'r'c'/'s't'y'l'e'.'c's's'`' 't'h'a't' 'i'm'p'o'r't's' 'T'a'i'l'w'i'n'd' 'C'S'S'.'

*style.css*
```css
@import "tailwindcss";
```

#### Step 7: Start your build process

'R'u'n' 'y'o'u'r' 'b'u'i'l'd' 'p'r'o'c'e's's' 'w'i't'h' '`'n'p'm' 'r'u'n' 'd'e'v'`'.'

*Terminal*
```shell
npm run dev
```

#### Step 8: Start using Tailwind in your project

'S't'a'r't' 'u's'i'n'g' 'T'a'i'l'w'i'n'd'''s' 'u't'i'l'i't'y' 'c'l'a's's'e's' 't'o' 's't'y'l'e' 'y'o'u'r' 'c'o'n't'e'n't'.'

*App.jsx*
```jsx
export default function App() {
          return (
            // [!code highlight:4]
            <h1 className="text-3xl font-bold underline">
              Hello world!
            </h1>
          )
        }
```

#### Step 9: Start using Tailwind in your project

'S't'a'r't' 'u's'i'n'g' 'T'a'i'l'w'i'n'd'''s' 'u't'i'l'i't'y' 'c'l'a's's'e's' 't'o' 's't'y'l'e' 'y'o'u'r' 'c'o'n't'e'n't'.'

*App.vue*
```vue
<template>
          <!-- [!code highlight:4] -->
          <h1 class="text-3xl font-bold underline">
            <!-- prettier-ignore -->
            Hello world!
          </h1>
        </template>
```

---

### <a id="ruby-on-rails"></a>Install Tailwind CSS with Ruby on Rails

Setting up Tailwind CSS in Ruby on Rails v8+ project.

#### Step 1: Create your project

'S't'a'r't' 'b'y' 'c'r'e'a't'i'n'g' 'a' 'n'e'w' 'R'a'i'l's' 'p'r'o'j'e'c't' 'i'f' 'y'o'u' 'd'o'n'''t' 'h'a'v'e' 'o'n'e' 's'e't' 'u'p' 'a'l'r'e'a'd'y'.' 'T'h'e' 'm'o's't' 'c'o'm'm'o'n' 'a'p'p'r'o'a'c'h' 'i's' 't'o' 'u's'e' 't'h'e' '['R'a'i'l's' 'C'o'm'm'a'n'd' 'L'i'n'e']'('h't't'p's':'/'/'g'u'i'd'e's'.'r'u'b'y'o'n'r'a'i'l's'.'o'r'g'/'c'o'm'm'a'n'd'_'l'i'n'e'.'h't'm'l')'.'

*Terminal*
```shell
rails new my-project
        cd my-project
```

#### Step 2: Install Tailwind CSS

'I'n's't'a'l'l' 't'h'e' '`'t'a'i'l'w'i'n'd'c's's'-'r'a'i'l's'`' 'g'e'm' 't'h'e'n' 'r'u'n' 't'h'e' 'i'n's't'a'l'l' 'c'o'm'm'a'n'd' 't'o' 's'e't' 'u'p' 'T'a'i'l'w'i'n'd' 'C'S'S' 'i'n' 'y'o'u'r' 'p'r'o'j'e'c't'.'

*Terminal*
```shell
bundle add tailwindcss-rails
        ./bin/rails tailwindcss:install
```

#### Step 3: Start your build process

'R'u'n' 'y'o'u'r' 'b'u'i'l'd' 'p'r'o'c'e's's' 'w'i't'h' '`'.'/'b'i'n'/'d'e'v'`'.'

*Terminal*
```shell
./bin/dev
```

#### Step 4: Start using Tailwind in your project

'S't'a'r't' 'u's'i'n'g' 'T'a'i'l'w'i'n'd'''s' 'u't'i'l'i't'y' 'c'l'a's's'e's' 't'o' 's't'y'l'e' 'y'o'u'r' 'c'o'n't'e'n't'.'

*index.html.erb*
```html
<!-- [!code highlight:4] -->
        <h1 class="text-3xl font-bold underline">
          <!-- prettier-ignore -->
          Hello world!
        </h1>
```

---

### <a id="solidjs"></a>Install Tailwind CSS with SolidJS

Setting up Tailwind CSS in a SolidJS project.

#### Step 1: Create your project

'S't'a'r't' 'b'y' 'c'r'e'a't'i'n'g' 'a' 'n'e'w' 'S'o'l'i'd'J'S' 'p'r'o'j'e'c't' 'i'f' 'y'o'u' 'd'o'n'''t' 'h'a'v'e' 'o'n'e' 's'e't' 'u'p' 'a'l'r'e'a'd'y'.' 'T'h'e' 'm'o's't' 'c'o'm'm'o'n' 'a'p'p'r'o'a'c'h' 'i's' 't'o' 'u's'e' '['t'h'e' 'S'o'l'i'd'J'S' 'V'i't'e' 't'e'm'p'l'a't'e']'('h't't'p's':'/'/'w'w'w'.'s'o'l'i'd'j's'.'c'o'm'/'g'u'i'd'e's'/'g'e't't'i'n'g'-'s't'a'r't'e'd')'.'

*Terminal*
```shell
npx degit solidjs/templates/js my-project
        cd my-project
```

#### Step 2: Install Tailwind CSS

'I'n's't'a'l'l' '`'@'t'a'i'l'w'i'n'd'c's's'/'v'i't'e'`' 'a'n'd' 'i't's' 'p'e'e'r' 'd'e'p'e'n'd'e'n'c'i'e's' 'v'i'a' 'n'p'm'.'

*Terminal*
```shell
npm install tailwindcss @tailwindcss/vite
```

#### Step 3: Configure Vite Plugin

'A'd'd' 't'h'e' '`'@'t'a'i'l'w'i'n'd'c's's'/'v'i't'e'`' 'p'l'u'g'i'n' 't'o' 'y'o'u'r' 'V'i't'e' 'c'o'n'f'i'g'u'r'a't'i'o'n'.'

*vite.config.ts*
```ts
import { defineConfig } from 'vite';
        import solidPlugin from 'vite-plugin-solid';
        // [!code highlight:2]
        import tailwindcss from '@tailwindcss/vite';

        export default defineConfig({
          plugins: [
            // [!code highlight:2]
            tailwindcss(),
            solidPlugin(),
          ],
          server: {
            port: 3000,
          },
          build: {
            target: 'esnext',
          },
        });
```

#### Step 4: Import Tailwind CSS

'A'd'd' 'a'n' '`'@'i'm'p'o'r't'`' 't'o' '`'.'/'s'r'c'/'i'n'd'e'x'.'c's's'`' 't'h'a't' 'i'm'p'o'r't's' 'T'a'i'l'w'i'n'd' 'C'S'S'.'

*index.css*
```css
@import "tailwindcss";
```

#### Step 5: Start your build process

'R'u'n' 'y'o'u'r' 'b'u'i'l'd' 'p'r'o'c'e's's' 'w'i't'h' '`'n'p'm' 'r'u'n' 'd'e'v'`'.'

*Terminal*
```shell
npm run dev
```

#### Step 6: Start using Tailwind in your project

'S't'a'r't' 'u's'i'n'g' 'T'a'i'l'w'i'n'd'''s' 'u't'i'l'i't'y' 'c'l'a's's'e's' 't'o' 's't'y'l'e' 'y'o'u'r' 'c'o'n't'e'n't'.'

*App.jsx*
```jsx
export default function App() {
          return (
            // [!code highlight:4]
            <h1 class="text-3xl font-bold underline">
              Hello world!
            </h1>
          )
        }
```

---

### <a id="sveltekit"></a>Install Tailwind CSS with SvelteKit

Setting up Tailwind CSS in a SvelteKit project.

#### Step 1: Create your project

'S't'a'r't' 'b'y' 'c'r'e'a't'i'n'g' 'a' 'n'e'w' 'S'v'e'l't'e'K'i't' 'p'r'o'j'e'c't' 'i'f' 'y'o'u' 'd'o'n'''t' 'h'a'v'e' 'o'n'e' 's'e't' 'u'p' 'a'l'r'e'a'd'y'.' 'T'h'e' 'm'o's't' 'c'o'm'm'o'n' 'a'p'p'r'o'a'c'h' 'i's' 'o'u't'l'i'n'e'd' 'i'n' 't'h'e' '['S'v'e'l't'e'K'i't']'('h't't'p's':'/'/'s'v'e'l't'e'.'d'e'v'/'d'o'c's'/'k'i't'/'c'r'e'a't'i'n'g'-'a'-'p'r'o'j'e'c't')' 'd'o'c'u'm'e'n't'a't'i'o'n'.'

*Terminal*
```shell
npx sv create my-project
        cd my-project
```

#### Step 2: Install Tailwind CSS

'I'n's't'a'l'l' '`'@'t'a'i'l'w'i'n'd'c's's'/'v'i't'e'`' 'a'n'd' 'i't's' 'p'e'e'r' 'd'e'p'e'n'd'e'n'c'i'e's' 'v'i'a' 'n'p'm'.'

*Terminal*
```shell
npm install tailwindcss @tailwindcss/vite
```

#### Step 3: Configure Vite Plugin

'A'd'd' 't'h'e' '`'@'t'a'i'l'w'i'n'd'c's's'/'v'i't'e'`' 'p'l'u'g'i'n' 't'o' 'y'o'u'r' 'V'i't'e' 'c'o'n'f'i'g'u'r'a't'i'o'n'.'

*vite.config.ts*
```ts
import { sveltekit } from '@sveltejs/kit/vite';
        import { defineConfig } from 'vite';
        // [!code highlight:2]
        import tailwindcss from '@tailwindcss/vite';

        export default defineConfig({
          plugins: [
            // [!code highlight:2]
            tailwindcss(),
            sveltekit(),
          ],
        });
```

#### Step 4: Import Tailwind CSS

'C'r'e'a't'e' 'a' '`'.'/'s'r'c'/'a'p'p'.'c's's'`' 'f'i'l'e' 'a'n'd' 'a'd'd' 'a'n' '`'@'i'm'p'o'r't'`' 't'h'a't' 'i'm'p'o'r't's' 'T'a'i'l'w'i'n'd' 'C'S'S'.'

*app.css*
```css
@import "tailwindcss";
```

#### Step 5: Import the CSS file

'C'r'e'a't'e' 'a' '`'.'/'s'r'c'/'r'o'u't'e's'/'+'l'a'y'o'u't'.'s'v'e'l't'e'`' 'f'i'l'e' 'a'n'd' 'i'm'p'o'r't' 't'h'e' 'n'e'w'l'y'-'c'r'e'a't'e'd' '`'a'p'p'.'c's's'`' 'f'i'l'e'.'

*+layout.svelte*
```svelte
<script>
          let { children } = $props();
          // [!code highlight:2]
          import "../app.css";
        </script>

        {@render children()}
```

#### Step 6: Start your build process

'R'u'n' 'y'o'u'r' 'b'u'i'l'd' 'p'r'o'c'e's's' 'w'i't'h' '`'n'p'm' 'r'u'n' 'd'e'v'`'.'

*Terminal*
```shell
npm run dev
```

#### Step 7: Start using Tailwind in your project

'S't'a'r't' 'u's'i'n'g' 'T'a'i'l'w'i'n'd'''s' 'u't'i'l'i't'y' 'c'l'a's's'e's' 't'o' 's't'y'l'e' 'y'o'u'r' 'c'o'n't'e'n't',' 'm'a'k'i'n'g' 's'u'r'e' 't'o' 'i'm'p'o'r't' 'y'o'u'r' 'T'a'i'l'w'i'n'd' 'C'S'S' 't'h'e'm'e' 'f'o'r' 'a'n'y' '`'&'l't';'s't'y'l'e'&'g't';'`' 'b'l'o'c'k's' 't'h'a't' 'n'e'e'd' 't'o' 'b'e' 'p'r'o'c'e's's'e'd' 'b'y' 'T'a'i'l'w'i'n'd'.'

*+page.svelte*
```svelte
<!-- [!code highlight:4] -->
        <h1 class="text-3xl font-bold underline">
          <!-- prettier-ignore -->
          Hello world!
        </h1>

        <style lang="postcss">
          /* [!code highlight:2] */
          @reference "tailwindcss";

          :global(html) {
            background-color: theme(--color-gray-100);
          }
        </style>
```

---

### <a id="symfony"></a>Install Tailwind CSS with Symfony

Setting up Tailwind CSS in a Symfony project.

#### Step 1: Create your project

'S't'a'r't' 'b'y' 'c'r'e'a't'i'n'g' 'a' 'n'e'w' 'S'y'm'f'o'n'y' 'p'r'o'j'e'c't' 'i'f' 'y'o'u' 'd'o'n'''t' 'h'a'v'e' 'o'n'e' 's'e't' 'u'p' 'a'l'r'e'a'd'y'.' 'T'h'e' 'm'o's't' 'c'o'm'm'o'n' 'a'p'p'r'o'a'c'h' 'i's' 't'o' 'u's'e' '['t'h'e' 'S'y'm'f'o'n'y' 'I'n's't'a'l'l'e'r']'('h't't'p's':'/'/'s'y'm'f'o'n'y'.'c'o'm'/'d'o'w'n'l'o'a'd')'.'

*Terminal*
```shell
symfony new --webapp my-project
        cd my-project
```

#### Step 2: Install Webpack Encore

'I'n's't'a'l'l' 'W'e'b'p'a'c'k' 'E'n'c'o'r'e',' 'w'h'i'c'h' 'h'a'n'd'l'e's' 'b'u'i'l'd'i'n'g' 'y'o'u'r' 'a's's'e't's'.' 'S'e'e' '['t'h'e' 'd'o'c'u'm'e'n't'a't'i'o'n']'('h't't'p's':'/'/'s'y'm'f'o'n'y'.'c'o'm'/'d'o'c'/'c'u'r'r'e'n't'/'f'r'o'n't'e'n'd'.'h't'm'l')' 'f'o'r' 'm'o'r'e' 'i'n'f'o'r'm'a't'i'o'n'.'

*Terminal*
```shell
composer remove symfony/ux-turbo symfony/asset-mapper symfony/stimulus-bundle
        composer require symfony/webpack-encore-bundle symfony/ux-turbo symfony/stimulus-bundle
```

#### Step 3: Install Tailwind CSS

'U's'i'n'g' 'n'p'm',' 'i'n's't'a'l'l' '`'@'t'a'i'l'w'i'n'd'c's's'/'p'o's't'c's's'`' 'a'n'd' 'i't's' 'p'e'e'r' 'd'e'p'e'n'd'e'n'c'i'e's',' 'a's' 'w'e'l'l' 'a's' '`'p'o's't'c's's'-'l'o'a'd'e'r'`'.'

*Terminal*
```shell
npm install tailwindcss @tailwindcss/postcss postcss postcss-loader
```

#### Step 4: Enable PostCSS support

'I'n' 'y'o'u'r' '`'w'e'b'p'a'c'k'.'c'o'n'f'i'g'.'j's'`' 'f'i'l'e',' 'e'n'a'b'l'e' 't'h'e' 'P'o's't'C'S'S' 'L'o'a'd'e'r'.' 'S'e'e' '['t'h'e' 'd'o'c'u'm'e'n't'a't'i'o'n']'('h't't'p's':'/'/'s'y'm'f'o'n'y'.'c'o'm'/'d'o'c'/'c'u'r'r'e'n't'/'f'r'o'n't'e'n'd'/'e'n'c'o'r'e'/'p'o's't'c's's'.'h't'm'l')' 'f'o'r' 'm'o'r'e' 'i'n'f'o'r'm'a't'i'o'n'.'

*webpack.config.js*
```js
Encore
          .enablePostCssLoader()
        ;
```

#### Step 5: Configure PostCSS Plugins

'C'r'e'a't'e' 'a' '`'p'o's't'c's's'.'c'o'n'f'i'g'.'m'j's'`' 'f'i'l'e' 'i'n' 't'h'e' 'r'o'o't' 'o'f' 'y'o'u'r' 'p'r'o'j'e'c't' 'a'n'd' 'a'd'd' 't'h'e' '`'@'t'a'i'l'w'i'n'd'c's's'/'p'o's't'c's's'`' 'p'l'u'g'i'n' 't'o' 'y'o'u'r' 'P'o's't'C'S'S' 'c'o'n'f'i'g'u'r'a't'i'o'n'.'

*postcss.config.mjs*
```js
export default {
          plugins: {
            // [!code highlight:2]
            "@tailwindcss/postcss": {},
          },
        };
```

#### Step 6: Import Tailwind CSS

'A'd'd' 'a'n' '`'@'i'm'p'o'r't'`' 't'o' '`'.'/'a's's'e't's'/'s't'y'l'e's'/'a'p'p'.'c's's'`' 't'h'a't' 'i'm'p'o'r't's' 'T'a'i'l'w'i'n'd' 'C'S'S' 'a'n'd' 'a'n' '`'@'s'o'u'r'c'e'`' 't'h'a't' 'i'g'n'o'r'e's' 't'h'e' 'p'u'b'l'i'c' 'd'i'r' 't'o' 'p'r'e'v'e'n't' 'r'e'c'o'm'p'i'l'e' 'l'o'o'p's' 'i'n' 'w'a't'c'h' 'm'o'd'e'.'

*app.css*
```css
@import "tailwindcss";
        @source not "../../public";
```

#### Step 7: Start your build process

'R'u'n' 'y'o'u'r' 'b'u'i'l'd' 'p'r'o'c'e's's' 'w'i't'h' '`'n'p'm' 'r'u'n' 'w'a't'c'h'`'.'

*Terminal*
```shell
npm run watch
```

#### Step 8: Start using Tailwind in your project

'M'a'k'e' 's'u'r'e' 'y'o'u'r' 'c'o'm'p'i'l'e'd' 'C'S'S' 'i's' 'i'n'c'l'u'd'e'd' 'i'n' 't'h'e' '`'<'h'e'a'd'>'`' 't'h'e'n' 's't'a'r't' 'u's'i'n'g' 'T'a'i'l'w'i'n'd'''s' 'u't'i'l'i't'y' 'c'l'a's's'e's' 't'o' 's't'y'l'e' 'y'o'u'r' 'c'o'n't'e'n't'.'

---

### <a id="tanstack-start"></a>Install Tailwind CSS with TanStack Start

Setting up Tailwind CSS in a TanStack Start project.

#### Step 1: Create project

'S't'a'r't' 'b'y' 'c'r'e'a't'i'n'g' 'a' 'n'e'w' 'T'a'n'S't'a'c'k' 'S't'a'r't' 'p'r'o'j'e'c't' 'i'f' 'y'o'u' 'd'o'n'''t' 'h'a'v'e' 'o'n'e' 's'e't' 'u'p' 'a'l'r'e'a'd'y'.' 'T'h'e' 'm'o's't' 'c'o'm'm'o'n' 'a'p'p'r'o'a'c'h' 'i's' 't'o' 'u's'e' '['C'r'e'a't'e' 'S't'a'r't' 'A'p'p']'('h't't'p's':'/'/'t'a'n's't'a'c'k'.'c'o'm'/'s't'a'r't'/'l'a't'e's't'/'d'o'c's'/'f'r'a'm'e'w'o'r'k'/'r'e'a'c't'/'o'v'e'r'v'i'e'w')'.'

*Terminal*
```shell
npx create-start-app@latest my-project
        cd my-project
```

#### Step 2: Install Tailwind CSS

'I'n's't'a'l'l' '`'@'t'a'i'l'w'i'n'd'c's's'/'v'i't'e'`' 'a'n'd' 'i't's' 'p'e'e'r' 'd'e'p'e'n'd'e'n'c'i'e's' 'v'i'a' 'n'p'm'.'

*Terminal*
```shell
npm install tailwindcss @tailwindcss/vite
```

#### Step 3: Configure Vite Plugin

'A'd'd' 't'h'e' '`'@'t'a'i'l'w'i'n'd'c's's'/'v'i't'e'`' 'p'l'u'g'i'n' 't'o' 'y'o'u'r' 'V'i't'e' 'c'o'n'f'i'g'u'r'a't'i'o'n'.'

*vite.config.ts*
```ts
import { tanstackStart } from '@tanstack/react-start/plugin/vite';
        import { defineConfig } from 'vite';
        import tsConfigPaths from 'vite-tsconfig-paths';
        // [!code highlight:2]
        import tailwindcss from '@tailwindcss/vite'

        export default defineConfig({
          plugins: [
            // [!code highlight:2]
            tailwindcss()
            tanstackStart(),
            tsConfigPaths(),
          ]
        });
```

#### Step 4: Import Tailwind CSS

'A'd'd' 'a'n' '`'@'i'm'p'o'r't'`' 't'o' '`'.'/'s'r'c'/'s't'y'l'e's'.'c's's'`' 't'h'a't' 'i'm'p'o'r't's' 'T'a'i'l'w'i'n'd' 'C'S'S'.'

*src/styles.css*
```css
@import "tailwindcss";
```

#### Step 5: Import the CSS file in your root route

'I'm'p'o'r't' 't'h'e' 'C'S'S' 'f'i'l'e' 'i'n' 'y'o'u'r' '`'_'_'r'o'o't'.'t's'x'`' 'f'i'l'e' 'w'i't'h' 't'h'e' '`'?'u'r'l'`' 'q'u'e'r'y'.'

*src/routes/__root.tsx*
```tsx
// other imports...

        // [!code highlight:2]
        import appCss from '../styles.css?url'

        export const Route = createRootRoute({
          head: () => ({
            meta: [
              // your meta tags and site config
            ],
            // [!code highlight:2]
            links: [{ rel: 'stylesheet', href: appCss }],
            // other head config
          }),
          component: RootComponent,
        })
```

#### Step 6: Start using Tailwind in your project

'S't'a'r't' 'u's'i'n'g' 'T'a'i'l'w'i'n'd'''s' 'u't'i'l'i't'y' 'c'l'a's's'e's' 't'o' 's't'y'l'e' 'y'o'u'r' 'c'o'n't'e'n't'.'

*src/routes/index.tsx*
```tsx
import { createFileRoute } from '@tanstack/react-router'

        export const Route = createFileRoute('/')({
          component: App,
        })

        function App() {
          return (
            // [!code highlight:4]
            <h1 class="text-3xl font-bold underline">
              Hello World!
            </h1>
          )
        }
```

---

