# Tailwind CSS v4.3 安装指南 (Scope A)

此文档包含从官方文档直接编译的所有 Tailwind CSS 安装指南和框架设置说明的合并集合。

## 目录

- [常规指南](#常规指南)
  - [Tailwind CLI](#tailwind-cli)
  - [Using PostCSS](#using-postcss)
  - [Using Vite](#using-vite)
  - [Play CDN](#play-cdn)
- [框架特定指南](#框架特定指南)
  - [阿多尼斯JS](#adonisjs)
  - [角](#angular)
  - [阿斯特罗](#astro)
  - [Ember.js](#emberjs)
  - [盖茨比](#gatsby)
  - [拉维尔](#laravel)
  - [流星](#meteor)
  - [Next.js](#nextjs)
  - [努克斯特](#nuxtjs)
  - [包裹](#parcel)
  - [凤凰](#phoenix)
  - [奎克](#qwik)
  - [反应路由器](#react-router)
  - [RS包](#rspack)
  - [红宝石 on Rails](#ruby-on-rails)
  - [SolidJS](#solidjs)
  - [苗条套件](#sveltekit)
  - [交响乐团](#symfony)
  - [TanStack 启动](#tanstack-start)

---

## <a id="常规指南"></a>常规指南

### Tailwind CLI

从头开始使用 Tailwind CSS 最简单、最快的方法是使用 Tailwind CLI 工具。

#### 步骤 1: 安装 Tailwind CSS

'通'过'`'n'p'm'`'安'装'`'t'a'i'l'w'i'n'd'c's's'和'@'t'a'i'l'w'i'n'd'c's's'/'c'l'i'`'。'

#### 步骤 2: 在 CSS 中导入 Tailwind

'将'`'@' 'i'm'p'o'r't' '“'t'a'i'l'w'i'n'd'c's's'”';'`'导'入'到'您'的'主'C'S'S'文'件'。'

#### 步骤 3: 启动 Tailwind CLI 构建过程

'R'u'n' 't'h'e' 'C'L'I' 't'o'o'l' 't'o' 's'c'a'n' 'y'o'u'r' 's'o'u'r'c'e' 'f'i'l'e's' 'f'o'r' 'c'l'a's's'e's' 'a'n'd' 'b'u'i'l'd' 'y'o'u'r' 'C'S'S'.'

#### 步骤 4: 开始在 HTML 中使用 Tailwind

'将'已'编'译'的'C'S'S'文'件'添'加'到'，'`'<'h'e'a'd'>'`'并'开'始'使'用'T'a'i'l'w'i'n'd'的'实'用'程'序'类'来'设'置'内'容'的'样'式'。'

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

### 使用 PostCSS 安装 Tailwind CSS

将 Tailwind CSS 作为 PostCSS 插件安装是将其与 Next.js 和 Angular 等框架集成的最无缝方式。

#### 步骤 1: 安装 Tailwind CSS

'通'过'`'n'p'm'`'安'装'`'t'a'i'l'w'i'n'd'c's's'、'@'t'a'i'l'w'i'n'd'c's's'/'`' '`'p'o's't'c's's'`'和'p'o's't'c's's'。'

*Terminal*
```shell
npm install tailwindcss @tailwindcss/postcss postcss
```

#### 步骤 2: 将 Tailwind 添加到您的 PostCSS 配置中

'将'`'@'t'a'i'l'w'i'n'd'c's's'/'`'p'o's't'c's's'添'加'`'到'`'p'o's't'c's's'.'c'o'n'f'i'g'.'m'j's'文'件'或'项'目'中'配'置'P'o's't'C'S'S'的'任'何'位'置'。'

*postcss.config.mjs*
```js
export default {
          plugins: {
            // [!code highlight:2]
            "@tailwindcss/postcss": {},
          }
        }
```

#### 步骤 3: 导入 Tailwind CSS

'在'`'导'入'顺'风'C'S'S'的'C'S'S'文'件'中'添'加'@' 'i'm'p'o'r't'`'。'

*CSS*
```css
@import "tailwindcss";
```

#### 步骤 4: 开始您的构建过程

'`'使'用'n'p'm' 'r'u'n' 'd'e'v'`'或'在'p'a'c'k'a'g'e'.'j's'o'n'文'件'中'配'置'的'任'何'命'令'运'行'构'`'`'建'过'程'。'

*Terminal*
```shell
npm run dev
```

#### 步骤 5: 开始在 HTML 中使用 Tailwind

'确'保'已'编'译'的'C'S'S'包'含'在'中'`'<'h'e'a'd'>'`'<'e'm'>'（'您'的'框'架'可'能'会'为'您'处'理'此'问'题'）'<'/'e'm'>' '，'然'后'开'始'使'用'T'a'i'l'w'i'n'd'的'实'用'程'序'类'来'设'置'内'容'的'样'式'。'

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

### 使用 Vite 安装 Tailwind CSS

将 Tailwind CSS 作为 Vite 插件安装是将其与 Laravel、SvelteKit、React Router、Nuxt 和 SolidJS 等框架集成的最无缝方式。

#### 步骤 1: 创建您的项目

'S't'a'r't' 'b'y' 'c'r'e'a't'i'n'g' 'a' 'n'e'w' 'V'i't'e' 'p'r'o'j'e'c't' 'i'f' 'y'o'u' 'd'o'n'''t' 'h'a'v'e' 'o'n'e' 's'e't' 'u'p' 'a'l'r'e'a'd'y'.' 'T'h'e' 'm'o's't' 'c'o'm'm'o'n' 'a'p'p'r'o'a'c'h' 'i's' 't'o' 'u's'e' '['C'r'e'a't'e' 'V'i't'e']'('h't't'p's':'/'/'v'i't'e'.'d'e'v'/'g'u'i'd'e'/'#'s'c'a'f'f'o'l'd'i'n'g'-'y'o'u'r'-'f'i'r's't'-'v'i't'e'-'p'r'o'j'e'c't')'.'

*Terminal*
```shell
npm create vite@latest my-project
        cd my-project
```

#### 步骤 2: 安装 Tailwind CSS

'通'过'`'n'p'm'`'安'装'`'t'a'i'l'w'i'n'd'c's's'和'@'t'a'i'l'w'i'n'd'c's's'/'v'i't'e'`'。'

*Terminal*
```shell
npm install tailwindcss @tailwindcss/vite
```

#### 步骤 3: 配置Vite插件

'将'`'@'t'a'i'l'w'i'n'd'c's's'/'v'i't'e'`'插'件'添'加'到'您'的'V'i't'e'配'置'中'。'

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

#### 步骤 4: 导入 Tailwind CSS

'在'`'导'入'顺'风'C'S'S'的'C'S'S'文'件'中'添'加'@' 'i'm'p'o'r't'`'。'

*CSS*
```css
@import "tailwindcss";
```

#### 步骤 5: 开始您的构建过程

'`'使'用'n'p'm' 'r'u'n' 'd'e'v'`'或'在'p'a'c'k'a'g'e'.'j's'o'n'文'件'中'配'置'的'任'何'命'令'运'行'构'`'`'建'过'程'。'

*Terminal*
```shell
npm run dev
```

#### 步骤 6: 开始在 HTML 中使用 Tailwind

'确'保'已'编'译'的'C'S'S'包'含'在'中'`'<'h'e'a'd'>'`'<'e'm'>'（'您'的'框'架'可'能'会'为'您'处'理'此'问'题'）'<'/'e'm'>' '，'然'后'开'始'使'用'T'a'i'l'w'i'n'd'的'实'用'程'序'类'来'设'置'内'容'的'样'式'。'

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

### 播放CDN

使用 Play CDN 直接在浏览器中尝试 Tailwind，无需任何构建步骤。

#### 步骤 1: 将 Play CDN 脚本添加到您的 HTML 中

'将'播'放'C'D'N'脚'本'标'签'添'加'到'H'T'M'L'文'件'的'`'&'l't';'h'e'a'd'&'g't';'`' '，'并'开'始'使'用'T'a'i'l'w'i'n'd'的'实'用'程'序'类'来'设'置'内'容'的'样'式'。'

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

#### 步骤 2: 尝试添加一些自定义 CSS

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

## <a id="框架特定指南"></a>框架特定指南

### <a id="adonisjs"></a>使用 AdonisJS 安装 Tailwind CSS

在 AdonisJS 项目中设置 Tailwind CSS。

#### 步骤 1: 创建您的项目

'如'果'您'还'没'有'设'置'一'个'新'的'A'd'o'n'i's'J'S'项'目'，'请'从'创'建'一'个'新'的'A'd'o'n'i's'J'S'项'目'开'始'。'最'常'见'的'方'法'是'使'用'['C'r'e'a't'e' 'A'd'o'n'i's'J'S']'('h't't'p's':'/'/'d'o'c's'.'a'd'o'n'i's'j's'.'c'o'm'/'g'u'i'd'e's'/'g'e't't'i'n'g'-'s't'a'r't'e'd'/'i'n's't'a'l'l'a't'i'o'n')'。'

*Terminal*
```shell
npm init adonisjs@latest my-project -- --kit=web
        cd my-project
```

#### 步骤 2: 安装 Tailwind CSS

'通'过'n'p'm'`'安'装'@'t'a'i'l'w'i'n'd'c's's'/'v'i't'e'`'及'其'对'等'依'赖'。'

*Terminal*
```shell
npm install tailwindcss @tailwindcss/vite
```

#### 步骤 3: 配置Vite插件

'将'`'@'t'a'i'l'w'i'n'd'c's's'/'v'i't'e'`'插'件'添'加'到'您'的'V'i't'e'配'置'中'。'

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

#### 步骤 4: 导入 Tailwind CSS

'将'`'@' 'i'm'p'o'r't'`'添'加'到'`'.'/'r'e's'o'u'r'c'e's'/'c's's'/'a'p'p'.'c's's'`' '，'用'于'导'入'顺'风'C'S'S'的'样'式'。'此'外'，'告'诉'T'a'i'l'w'i'n'd' 'C'S'S'扫'描'您'的'`'资'源'/'视'图'`'目'录'以'查'找'实'用'程'序'。'

*app.css*
```css
@import "tailwindcss";
        @source "../views";
```

#### 步骤 5: 开始您的构建过程

'使'用'`'n'p'm' 'r'u'n' 'd'e'v'运'行'`'构'建'过'程'。'

#### 步骤 6: 开始在您的项目中使用 Tailwind

'确'保'已'编'译'的'C'S'S'包'含'在'中'，'`'<'h'e'a'd'>'`'然'后'开'始'使'用'T'a'i'l'w'i'n'd'的'实'用'程'序'类'来'设'置'内'容'的'样'式'。'

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

### <a id="angular"></a>使用 Angular 安装 Tailwind CSS

在 Angular 项目中设置 Tailwind CSS。

#### 步骤 1: 创建您的项目

'如'果'您'还'没'有'设'置'一'个'新'的'A'n'g'u'l'a'r'项'目'，'请'从'创'建'一'个'新'的'A'n'g'u'l'a'r'项'目'开'始'。'最'常'见'的'方'法'是'使'用'['A'n'g'u'l'a'r' 'C'L'I']'('h't't'p's':'/'/'a'n'g'u'l'a'r'.'d'e'v'/'t'o'o'l's'/'c'l'i'/'s'e't'u'p'-'l'o'c'a'l')'。'

*Terminal*
```shell
ng new my-project --style css
        cd my-project
```

#### 步骤 2: 安装 Tailwind CSS

'(' '通'过'n'p'm'`'安'装'@'t'a'i'l'w'i'n'd'c's's'/'`'p'o's't'c's's'及'其'对'等'依'赖'。')','/'/'注'意'：' '`'-'-'f'o'r'c'e'`'标'志'用'于'确'保'安'装'成'功'。'A'n'g'u'l'a'r'对'''t'a'i'l'w'i'n'd'c's's'`' 'v'3'有'对'等'依'赖'，'在'安'装'`'t'a'i'l'w'i'n'd'c's's'`' 'v'4'时'会'导'致'错'误'。'代'码'：' '{'n'a'm'e':' '"'T'e'r'm'i'n'a'l'"',' 'l'a'n'g':' '"'s'h'e'l'l'"'

*Terminal*
```shell
npm install tailwindcss @tailwindcss/postcss postcss --force
```

#### 步骤 3: 配置 PostCSS 插件

'在'项'目'根'`'目'`'录'中'创'建'.'p'o's't'c's's'r'c'.'j's'o'n'文'件'，'并'将'`'@'t'a'i'l'w'i'n'd'c's's'/'p'o's't'c's's'`'插'件'添'加'到'P'o's't'C'S'S'配'置'中'。'

*.postcssrc.json*
```js
{
          "plugins": {
            // [!code highlight:2]
            "@tailwindcss/postcss": {}
          }
        }
```

#### 步骤 4: 导入 Tailwind CSS

'将'导'入'顺'风'C'S'S'的'`'@' 'i'm'p'o'r't'`'添'加'到'`'.'/'s'r'c'/'s't'y'l'e's'.'c's's'`'。'

*styles.css*
```css
@import "tailwindcss";
```

#### 步骤 5: 开始您的构建过程

'使'用'`'n'g' 's'e'r'v'e'`'运'行'构'建'过'程'。'

*Terminal*
```shell
ng serve
```

#### 步骤 6: 开始在您的项目中使用 Tailwind

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

### <a id="astro"></a>使用 Astro 安装 Tailwind CSS

在 Astro 项目中设置 Tailwind CSS。

#### 步骤 1: 创建您的项目

'如'果'您'还'没'有'设'置'一'个'新'的'A's't'r'o'项'目'，'请'从'创'建'一'个'新'的'A's't'r'o'项'目'开'始'。'最'常'见'的'方'法'是'使'用'['C'R'E'A'T'E' 'A'S'T'R'O']'('h't't'p's':'/'/'d'o'c's'.'a's't'r'o'.'b'u'i'l'd'/'e'n'/'i'n's't'a'l'l'-'a'n'd'-'s'e't'u'p'/'#'i'n's't'a'l'l'-'f'r'o'm'-'t'h'e'-'c'l'i'-'w'i'z'a'r'd')'。'

*Terminal*
```shell
npm create astro@latest my-project
        cd my-project
```

#### 步骤 2: 安装 Tailwind CSS

'通'过'n'p'm'`'安'装'@'t'a'i'l'w'i'n'd'c's's'/'v'i't'e'`'及'其'对'等'依'赖'。'

*Terminal*
```shell
npm install tailwindcss @tailwindcss/vite
```

#### 步骤 3: 配置Vite插件

'将'`'@'t'a'i'l'w'i'n'd'c's's'/'v'i't'e'`'插'件'添'加'到'A's't'r'o'配'置'文'件'中'的'V'i't'e'插'件'。'

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

#### 步骤 4: 导入 Tailwind CSS

'创'建'`'.'/'s'r'c'/'s't'y'l'e's'/'g'l'o'b'a'l'.'c's's'`'文'件'，'并'为'T'a'i'l'w'i'n'd' 'C'S'S'添'加'`'@' 'i'm'p'o'r't'`'。'

*global.css*
```css
@import "tailwindcss";
```

#### 步骤 5: 开始您的构建过程

'使'用'`'n'p'm' 'r'u'n' 'd'e'v'运'行'`'构'建'过'程'。'

*Terminal*
```shell
npm run dev
```

#### 步骤 6: 开始在您的项目中使用 Tailwind

'S't'a'r't' 'u's'i'n'g' 'T'a'i'l'w'i'n'd'''s' 'u't'i'l'i't'y' 'c'l'a's's'e's' 't'o' 's't'y'l'e' 'y'o'u'r' 'c'o'n't'e'n't' 'w'h'i'l'e' 'm'a'k'i'n'g' 's'u'r'e' 't'o' 'i'm'p'o'r't' 't'h'e' 'n'e'w'l'y' 'c'r'e'a't'e'd' 'C'S'S' 'f'i'l'e'.'

---

### <a id="emberjs"></a>使用 Ember.js 安装 Tailwind CSS

在 Ember.js 项目中设置 Tailwind CSS。

#### 步骤 1: 创建您的项目

'如'果'您'还'没'有'设'置'一'个'新'的'E'm'b'e'r'.'j's'项'目'，'请'从'创'建'一'个'新'的'E'm'b'e'r'.'j's'项'目'开'始'。'最'常'见'的'方'法'是'使'用'['E'm'b'e'r' 'C'L'I' ']'('h't't'p's':'/'/'g'u'i'd'e's'.'e'm'b'e'r'j's'.'c'o'm'/'r'e'l'e'a's'e'/'g'e't't'i'n'g'-'s't'a'r't'e'd'/'q'u'i'c'k'-'s't'a'r't'/'#'t'o'c'_'c'r'e'a't'e'-'a'-'n'e'w'-'a'p'p'l'i'c'a't'i'o'n')'。'

*Terminal*
```shell
npx ember-cli new my-project --embroider --no-welcome
        cd my-project
```

#### 步骤 2: 安装 Tailwind CSS

'U's'i'n'g' 'n'p'm',' 'i'n's't'a'l'l' '`'@'t'a'i'l'w'i'n'd'c's's'/'p'o's't'c's's'`' 'a'n'd' 'i't's' 'p'e'e'r' 'd'e'p'e'n'd'e'n'c'i'e's',' 'a's' 'w'e'l'l' 'a's' '`'p'o's't'c's's'-'l'o'a'd'e'r'`'.'

*Terminal*
```shell
npm install tailwindcss @tailwindcss/postcss postcss postcss-loader
```

#### 步骤 3: 启用 PostCSS 支持

'在'e'm'b'e'r'-'c'l'i'-'b'u'i'l'd'.'j's'`'文'件'`'中'，'配'置'P'o's't'C'S'S'以'处'理'C'S'S'文'件'。'

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

#### 步骤 4: 配置 PostCSS 插件

'在'项'目'根'`'目'`'录'中'创'建'p'o's't'c's's'.'c'o'n'f'i'g'.'m'j's'文'件'，'并'将'`'@'t'a'i'l'w'i'n'd'c's's'/'p'o's't'c's's'`'插'件'添'加'到'P'o's't'C'S'S'配'置'中'。'

*postcss.config.mjs*
```js
export default {
          plugins: {
            // [!code highlight:2]
            "@tailwindcss/postcss": {},
          },
        }
```

#### 步骤 5: 导入 Tailwind CSS

'创'建'一'个'`'.'/'a'p'p'/'a'p'p'.'c's's'`'文'件'，'并'为'T'a'i'l'w'i'n'd' 'C'S'S'添'加'一'个'`'@' 'i'm'p'o'r't'`'。'

*app.css*
```css
@import "tailwindcss";
```

#### 步骤 6: 导入 CSS 文件

'在'`'.'/'a'p'p'/'`' '`'a'p'p'.'j's'文'件'中'导'入'新'创'建'的'.'/'a'p'p'/'`'a'p'p'.'c's's'文'件'。'

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

#### 步骤 7: 开始您的构建过程

'使'用'`'n'p'm' 'r'u'n' 's't'a'r't'运'行'`'构'建'过'程'。'

*Terminal*
```shell
npm run start
```

#### 步骤 8: 开始在您的项目中使用 Tailwind

'S't'a'r't' 'u's'i'n'g' 'T'a'i'l'w'i'n'd'''s' 'u't'i'l'i't'y' 'c'l'a's's'e's' 't'o' 's't'y'l'e' 'y'o'u'r' 'c'o'n't'e'n't'.'

---

### <a id="gatsby"></a>使用 Gatsby 安装 Tailwind CSS

在 Gatsby 项目中设置 Tailwind CSS。

#### 步骤 1: 创建您的项目

'如'果'您'还'没'有'设'置'一'个'新'的'G'a't's'b'y'项'目'，'请'从'创'建'一'个'新'的'G'a't's'b'y'项'目'开'始'。'最'常'见'的'方'法'是'使'用'['G'a't's'b'y' 'C'L'I']'('h't't'p's':'/'/'w'w'w'.'g'a't's'b'y'j's'.'c'o'm'/'d'o'c's'/'r'e'f'e'r'e'n'c'e'/'g'a't's'b'y'-'c'l'i'/'#'h'o'w'-'t'o'-'u's'e'-'g'a't's'b'y'-'c'l'i')'。'

*Terminal*
```shell
gatsby new my-project
        cd my-project
```

#### 步骤 2: 安装 Tailwind CSS

'U's'i'n'g' 'n'p'm',' 'i'n's't'a'l'l' '`'@'t'a'i'l'w'i'n'd'c's's'/'p'o's't'c's's'`',' 'i't's' 'p'e'e'r' 'd'e'p'e'n'd'e'n'c'i'e's',' 'a'n'd' '`'g'a't's'b'y'-'p'l'u'g'i'n'-'p'o's't'c's's'`'.'

*Terminal*
```shell
npm install @tailwindcss/postcss tailwindcss postcss gatsby-plugin-postcss
```

#### 步骤 3: 启用 Gatsby PostCSS 插件

'在'g'a't's'b'y'-'c'o'n'f'i'g'.'j's'`'文'件'`'中'，'启'用'`'g'a't's'b'y'-'p'l'u'g'i'n'-'p'o's't'c's's'`'。'有'关'更'多'信'息'['，'请'参'阅'插'件'的'文'档']'('h't't'p's':'/'/'w'w'w'.'g'a't's'b'y'j's'.'c'o'm'/'p'l'u'g'i'n's'/'g'a't's'b'y'-'p'l'u'g'i'n'-'p'o's't'c's's'/')'。'

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

#### 步骤 4: 配置 PostCSS 插件

'在'项'目'根'目'录'中'创'建'`'p'o's't'c's's'.'c'o'n'f'i'g'.'j's'`'文'件'，'并'将'`'@'t'a'i'l'w'i'n'd'c's's'/'p'o's't'c's's'`'插'件'添'加'到'P'o's't'C'S'S'配'置'中'。'

*postcss.config.js*
```js
module.exports = {
          plugins: {
            // [!code highlight:2]
            "@tailwindcss/postcss": {},
          },
        };
```

#### 步骤 5: 导入 Tailwind CSS

'创'建'`'.'/'s'r'c'/'s't'y'l'e's'/'g'l'o'b'a'l'.'c's's'`'文'件'，'并'为'T'a'i'l'w'i'n'd' 'C'S'S'添'加'`'@' 'i'm'p'o'r't'`'。'

*global.css*
```css
@import "tailwindcss";
```

#### 步骤 6: 导入 CSS 文件

'在'项'目'根'`'目'`'录'下'创'建'一'个'g'a't's'b'y'-'b'r'o'w's'e'r'.'j's'文'件'（'如'果'该'文'件'尚'不'存'在'）' '，'然'后'导'入'新'创'建'的'`'.'/'s'r'c'/'s't'y'l'e's'/'g'l'o'b'a'l'.'c's's'`'文'件'。'

*gatsby-browser.js*
```js
import './src/styles/global.css';
```

#### 步骤 7: 开始您的构建过程

'使'用'`'g'a't's'b'y' 'd'e'v'e'l'o'p'`'运'行'构'建'过'程'。'

*Terminal*
```shell
gatsby develop
```

#### 步骤 8: 开始在您的项目中使用 Tailwind

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

### <a id="laravel"></a>使用 Laravel 安装 Tailwind CSS

在 Laravel 项目中设置 Tailwind CSS。

#### 步骤 1: 创建您的项目

'如'果'您'还'没'有'设'置'一'个'新'的'L'a'r'a'v'e'l'项'目'，'请'从'创'建'一'个'新'的'L'a'r'a'v'e'l'项'目'开'始'。'最'常'见'的'方'法'是'使'用'['L'a'r'a'v'e'l'安'装'程'序']'('h't't'p's':'/'/'l'a'r'a'v'e'l'.'c'o'm'/'d'o'c's'#'c'r'e'a't'i'n'g'-'a'n'-'a'p'p'l'i'c'a't'i'o'n')'。'

*Terminal*
```shell
laravel new my-project
        cd my-project
```

#### 步骤 2: 安装 Tailwind CSS

'通'过'n'p'm'`'安'装'@'t'a'i'l'w'i'n'd'c's's'/'v'i't'e'`'及'其'对'等'依'赖'。'

*Terminal*
```shell
npm install tailwindcss @tailwindcss/vite
```

#### 步骤 3: 安装 Tailwind CSS

'通'过'n'p'm'`'安'装'@'t'a'i'l'w'i'n'd'c's's'/'`'p'o's't'c's's'及'其'对'等'依'赖'。'

*Terminal*
```shell
npm install tailwindcss @tailwindcss/postcss postcss
```

#### 步骤 4: 配置Vite插件

'将'`'@'t'a'i'l'w'i'n'd'c's's'/'v'i't'e'`'插'件'添'加'到'您'的'V'i't'e'配'置'中'。'

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

#### 步骤 5: 将 Tailwind 添加到您的 Laravel Mix 配置中

'在'`'w'e'b'p'a'c'k'.'m'i'x'.'j's'`'文'件'中'，'将't'a'i'l'w'i'n'd'c's's'`'添'加'`'为'P'o's't'C'S'S'插'件'。'

*webpack.mix.js*
```js
mix
          .js("resources/js/app.js", "public/js")
          .postCss("resources/css/app.css", "public/css", [
            // [!code highlight:2]
            require("@tailwindcss/postcss"),
          ]);
```

#### 步骤 6: 导入 Tailwind CSS

'将'`'@' 'i'm'p'o'r't'`'添'加'到'`'.'/'r'e's'o'u'r'c'e's'/'c's's'/'a'p'p'.'c's's'`'以'导'入'顺'风'C'S'S'。'此'外'，'告'诉'T'a'i'l'w'i'n'd' 'C'S'S'扫'描'一'些'目'录'以'查'找'实'用'程'序'。'

*app.css*
```css
@import "tailwindcss";

        @source "../../vendor/laravel/framework/src/Illuminate/Pagination/resources/views/*.blade.php";
        @source "../../storage/framework/views/*.php";
        @source "../**/*.blade.php";
        @source "../**/*.js";
```

#### 步骤 7: 开始您的构建过程

'使'用'`'n'p'm' 'r'u'n' 'd'e'v'运'行'`'构'建'过'程'。'

*Terminal*
```shell
npm run dev
```

#### 步骤 8: 开始您的构建过程

'使'用'`'n'p'm' 'r'u'n' 'w'a't'c'h'运'行'`'构'建'过'程'。'

*Terminal*
```shell
npm run watch
```

#### 步骤 9: 开始在您的项目中使用 Tailwind

'确'保'已'编'译'的'C'S'S'包'含'在'中'，'`'<'h'e'a'd'>'`'然'后'开'始'使'用'T'a'i'l'w'i'n'd'的'实'用'程'序'类'来'设'置'内'容'的'样'式'。'

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

#### 步骤 10: 开始在您的项目中使用 Tailwind

'确'保'已'编'译'的'C'S'S'包'含'在'中'，'`'<'h'e'a'd'>'`'然'后'开'始'使'用'T'a'i'l'w'i'n'd'的'实'用'程'序'类'来'设'置'内'容'的'样'式'。'

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

### <a id="meteor"></a>使用 Meteor 安装 Tailwind CSS

在 Meteor 项目中设置 Tailwind CSS。

#### 步骤 1: 创建您的项目

'如'果'您'还'没'有'设'置'一'个'新'的'流'星'项'目'，'请'从'创'建'一'个'新'的'流'星'项'目'开'始'。'最'常'见'的'方'法'是'使'用'['M'e't'e'o'r' 'C'L'I']'('h't't'p's':'/'/'d'o'c's'.'m'e't'e'o'r'.'c'o'm'/'a'b'o'u't'/'i'n's't'a'l'l'.'h't'm'l')'。'

*Terminal*
```shell
npx meteor create my-project
        cd my-project
```

#### 步骤 2: 安装 Tailwind CSS

'通'过'n'p'm'`'安'装'@'t'a'i'l'w'i'n'd'c's's'/'`'p'o's't'c's's'及'其'对'等'依'赖'。'

*Terminal*
```shell
npm install tailwindcss @tailwindcss/postcss postcss postcss-load-config
```

#### 步骤 3: 配置 PostCSS 插件

'在'项'目'根'`'目'`'录'中'创'建'p'o's't'c's's'.'c'o'n'f'i'g'.'m'j's'文'件'，'并'将'`'@'t'a'i'l'w'i'n'd'c's's'/'p'o's't'c's's'`'插'件'添'加'到'P'o's't'C'S'S'配'置'中'。'

*postcss.config.mjs*
```js
export default {
          plugins: {
            // [!code highlight:2]
            "@tailwindcss/postcss": {},
          },
        };
```

#### 步骤 4: 导入 Tailwind CSS

'将'T'a'i'l'w'i'n'd' 'C'S'S'的'`'@' 'i'm'p'o'r't'`'添'加'到'`'.'/'c'l'i'e'n't'/'m'a'i'n'.'c's's'`'文'件'中'。'

*main.css*
```css
@import "tailwindcss";
```

#### 步骤 5: 开始您的构建过程

'使'用'`'n'p'm' 'r'u'n' 's't'a'r't'运'行'`'构'建'过'程'。'

*Terminal*
```shell
npm run start
```

#### 步骤 6: 开始在您的项目中使用 Tailwind

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

### <a id="nextjs"></a>使用 Next.js 安装 Tailwind CSS

在 Next.js 项目中设置 Tailwind CSS。

#### 步骤 1: 创建您的项目

'如'果'您'还'没'有'设'置'新'的'N'e'x't'.'j's'项'目'，'请'从'创'建'新'的'N'e'x't'.'j's'项'目'开'始'。'最'常'见'的'方'法'是'使'用'“'['创'建'下'一'个'应'用']'('h't't'p's':'/'/'n'e'x't'j's'.'o'r'g'/'d'o'c's'/'a'p'i'-'r'e'f'e'r'e'n'c'e'/'c'r'e'a't'e'-'n'e'x't'-'a'p'p')'”'。'

*Terminal*
```shell
npx create-next-app@latest my-project --typescript --eslint --app
        cd my-project
```

#### 步骤 2: 安装 Tailwind CSS

'通'过'n'p'm'`'安'装'@'t'a'i'l'w'i'n'd'c's's'/'`'p'o's't'c's's'及'其'对'等'依'赖'。'

*Terminal*
```shell
npm install tailwindcss @tailwindcss/postcss postcss
```

#### 步骤 3: 配置 PostCSS 插件

'在'项'目'根'`'目'`'录'中'创'建'p'o's't'c's's'.'c'o'n'f'i'g'.'m'j's'文'件'，'并'将'`'@'t'a'i'l'w'i'n'd'c's's'/'p'o's't'c's's'`'插'件'添'加'到'P'o's't'C'S'S'配'置'中'。'

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

#### 步骤 4: 导入 Tailwind CSS

'将'`'@' 'i'm'p'o'r't'添'加'到'导'入'`'顺'风'C'S'S'`'的'.'/'a'p'p'/'`'g'l'o'b'a'l's'.'c's's'。'

*globals.css*
```css
@import "tailwindcss";
```

#### 步骤 5: 开始您的构建过程

'使'用'`'n'p'm' 'r'u'n' 'd'e'v'运'行'`'构'建'过'程'。'

*Terminal*
```shell
npm run dev
```

#### 步骤 6: 开始在您的项目中使用 Tailwind

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

### <a id="nuxtjs"></a>使用 Nuxt 安装 Tailwind CSS

在 Nuxt 项目中设置 Tailwind CSS。

#### 步骤 1: 创建您的项目

'如'果'您'还'没'有'设'置'一'个'新'的'N'u'x't'项'目'，'请'从'创'建'一'个'新'的'N'u'x't'项'目'开'始'。'最'常'见'的'方'法'是'使'用'['C'r'e'a't'e' 'N'u'x't']'('h't't'p's':'/'/'n'u'x't'.'c'o'm'/'d'o'c's'/'4'.'x'/'g'e't't'i'n'g'-'s't'a'r't'e'd'/'i'n's't'a'l'l'a't'i'o'n'#'n'e'w'-'p'r'o'j'e'c't')'。'

*Terminal*
```shell
npm create nuxt my-project
        cd my-project
```

#### 步骤 2: 安装 Tailwind CSS

'通'过'n'p'm'`'安'装'@'t'a'i'l'w'i'n'd'c's's'/'v'i't'e'`'及'其'对'等'依'赖'。'

*Terminal*
```shell
npm install tailwindcss @tailwindcss/vite
```

#### 步骤 3: 配置Vite插件

'将'`'@'t'a'i'l'w'i'n'd'c's's'/'v'i't'e'`'插'件'作'为'V'i't'e'插'件'添'加'到'您'的'N'u'x't'配'置'中'。'

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

#### 步骤 4: 导入 Tailwind CSS

'创'建'一'个'`'.'/'a'p'p'/'a's's'e't's'/'c's's'/'m'a'i'n'.'c's's'`'文'件'，'并'添'加'一'个'导'入'T'a'i'l'w'i'n'd' 'C'S'S'的'`'@' 'i'm'p'o'r't'`'。'

*main.css*
```css
@import "tailwindcss";
```

#### 步骤 5: 全局添加CSS文件

'将'新'创'建'的'`'.'/'a'p'p'/'a's's'e't's'/'c's's'/'m'a'i'n'.'c's's'`'添'加'到'`'n'u'x't'.'c'o'n'f'i'g'.'t's'文'件'中'的'c's's'`'数'`'`'组'中'。'

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

#### 步骤 6: 开始您的构建过程

'使'用'`'n'p'm' 'r'u'n' 'd'e'v'运'行'`'构'建'过'程'。'

*Terminal*
```shell
npm run dev
```

#### 步骤 7: 开始在您的项目中使用 Tailwind

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

### <a id="parcel"></a>使用 Parcel 安装 Tailwind CSS

在 Parcel 项目中设置 Tailwind CSS。

#### 步骤 1: 创建您的项目

'如'果'您'还'没'有'设'置'一'个'新'的'P'a'r'c'e'l'项'目'，'请'从'创'建'一'个'新'的'P'a'r'c'e'l'项'目'开'始'。'最'常'见'的'方'法'是'将'P'a'r'c'e'l'作'为'开'发'依'赖'项'添'加'到'项'目'中'，'如'['入'门'指'南']'('h't't'p's':'/'/'p'a'r'c'e'l'j's'.'o'r'g'/'g'e't't'i'n'g'-'s't'a'r't'e'd'/'w'e'b'a'p'p'/')'中'所'述'。'

*Terminal*
```shell
mkdir my-project
        cd my-project
        npm init -y
        npm install parcel
        mkdir src
        touch src/index.html
```

#### 步骤 2: 安装 Tailwind CSS

'通'过'n'p'm'`'安'装'@'t'a'i'l'w'i'n'd'c's's'/'`'p'o's't'c's's'及'其'对'等'依'赖'。'

*Terminal*
```shell
npm install tailwindcss @tailwindcss/postcss
```

#### 步骤 3: 配置 PostCSS

'在'项'目'根'目'录'中'创'建'`'.'p'o's't'c's's'r'c'`'文'件'，'并'启'用'`'@'t'a'i'l'w'i'n'd'c's's'/'p'o's't'c's's'插'`'件'。'

*.postcssrc*
```json
{
          "plugins": {
            "@tailwindcss/postcss": {}
          }
        }
```

#### 步骤 4: 导入 Tailwind CSS

'创'建'一'个'`'.'/'s'r'c'/'i'n'd'e'x'.'c's's'`'文'件'，'并'为'T'a'i'l'w'i'n'd' 'C'S'S'添'加'一'个'`'@' 'i'm'p'o'r't'`'。'

*index.css*
```css
@import "tailwindcss";
```

#### 步骤 5: 开始您的构建过程

'使'用'`'n'p'x'包's'r'c'/'i'n'd'e'x'.'h't'm'l'运'行'构'建'过'程'`'。'

*Terminal*
```shell
npx parcel src/index.html
```

#### 步骤 6: 开始在您的项目中使用 Tailwind

'将'C'S'S'文'件'添'加'到'，'`'<'h'e'a'd'>'`'并'开'始'使'用'T'a'i'l'w'i'n'd'的'实'用'程'序'类'来'设'置'内'容'的'样'式'。'

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

### <a id="phoenix"></a>使用 Phoenix 安装 Tailwind CSS

在 Phoenix 项目中设置 Tailwind CSS。

#### 步骤 1: 创建您的项目

'S't'a'r't' 'b'y' 'c'r'e'a't'i'n'g' 'a' 'n'e'w' 'P'h'o'e'n'i'x' 'p'r'o'j'e'c't' 'i'f' 'y'o'u' 'd'o'n'''t' 'h'a'v'e' 'o'n'e' 's'e't' 'u'p' 'a'l'r'e'a'd'y'.' 'Y'o'u' 'c'a'n' 'f'o'l'l'o'w' 't'h'e'i'r' '['i'n's't'a'l'l'a't'i'o'n' 'g'u'i'd'e']'('h't't'p's':'/'/'h'e'x'd'o'c's'.'p'm'/'p'h'o'e'n'i'x'/'i'n's't'a'l'l'a't'i'o'n'.'h't'm'l')' 't'o' 'g'e't' 'u'p' 'a'n'd' 'r'u'n'n'i'n'g'.'

*Terminal*
```shell
mix phx.new myproject
        cd myproject
```

#### 步骤 2: 安装 Tailwind 插件

'将'T'a'i'l'w'i'n'd'插'件'添'加'到'依'赖'项'中'，'并'`'运'行'm'i'x'`' 'd'e'p's'.'g'e't'进'行'安'装'。'

#### 步骤 3: 配置 Tailwind 插件

'在'`'c'o'n'f'i'g'/'c'o'n'f'i'g'.'e'x's'文'件'`'中'，'您'可'以'设'置'要'使'用'的'T'a'i'l'w'i'n'd' 'C'S'S'版'本'并'自'定'义'资'产'路'径'。'

#### 步骤 4: 更新您的部署脚本

'配'置'您'的'`'a's's'e't's'.'d'e'p'l'o'y'`'别'名'以'在'部'署'时'构'建'C'S'S'。'

#### 步骤 5: 在开发中启用观察者

'将'T'a'i'l'w'i'n'd'添'加'到'`'.'/'c'o'n'f'i'g'/'`'d'e'v'.'e'x's'文'件'中'的'观'察'者'列'表'中'。'

#### 步骤 6: 安装 Tailwind CSS

'R'u'n' 't'h'e' 'i'n's't'a'l'l' 'c'o'm'm'a'n'd' 't'o' 'd'o'w'n'l'o'a'd' 't'h'e' 's't'a'n'd'a'l'o'n'e' 'T'a'i'l'w'i'n'd' 'C'L'I'.'

*Terminal*
```shell
mix tailwind.install
```

#### 步骤 7: 导入 Tailwind CSS

'将'`'@' 'i'm'p'o'r't'`'添'加'到'`'.'/'a's's'e't's'/'c's's'/'a'p'p'.'c's's'`'以'导'入'顺'风'C'S'S'。'

*app.css*
```css
@import "tailwindcss";
```

#### 步骤 8: 删除默认的 CSS 导入

'从'`'.'/'a's's'e't's'/'j's'/'a'p'p'.'j's'`'中'删'除'C'S'S'导'入'，'因'为'T'a'i'l'w'i'n'd'现'在'正'在'为'您'处'理'此'操'作'。'

*app.js*
```js
// [!code --:3]
        // Remove this line if you add your own CSS build pipeline (e.g postcss).
        import "../css/app.css"
```

#### 步骤 9: 开始您的构建过程

'使'用'`'m'i'x' 'p'h'x'.'s'e'r'v'e'r'运'行'构'建'过'程'`'。'

*Terminal*
```shell
mix phx.server
```

#### 步骤 10: 开始在您的项目中使用 Tailwind

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

### <a id="qwik"></a>使用 Qwik 安装 Tailwind CSS

在 Qwik 项目中设置 Tailwind CSS。

#### 步骤 1: 创建您的项目

'S't'a'r't' 'b'y' 'c'r'e'a't'i'n'g' 'a' 'n'e'w' 'Q'w'i'k' 'p'r'o'j'e'c't' 'i'f' 'y'o'u' 'd'o'n'''t' 'h'a'v'e' 'o'n'e' 's'e't' 'u'p' 'a'l'r'e'a'd'y'.' 'T'h'e' 'm'o's't' 'c'o'm'm'o'n' 'a'p'p'r'o'a'c'h' 'i's' 't'o' 'u's'e' '['C'r'e'a't'e' 'Q'w'i'k']'('h't't'p's':'/'/'q'w'i'k'.'d'e'v'/'d'o'c's'/'g'e't't'i'n'g'-'s't'a'r't'e'd'/'#'c'r'e'a't'e'-'a'n'-'a'p'p'-'u's'i'n'g'-'t'h'e'-'c'l'i')'.'

*Terminal*
```shell
npm create qwik@latest empty my-project
        cd my-project
```

#### 步骤 2: 安装 Tailwind CSS

'通'过'n'p'm'`'安'装'@'t'a'i'l'w'i'n'd'c's's'/'v'i't'e'`'及'其'对'等'依'赖'。'

*Terminal*
```shell
npm install tailwindcss @tailwindcss/vite
```

#### 步骤 3: 配置Vite插件

'将'`'@'t'a'i'l'w'i'n'd'c's's'/'v'i't'e'`'插'件'添'加'到'您'的'V'i't'e'配'置'中'。'

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

#### 步骤 4: 导入 Tailwind CSS

'将'`'@' 'i'm'p'o'r't'添'加'到'导'入'`'顺'风'C'S'S'的'`'.'/'s'r'c'/'g'l'o'b'a'l'.'c's's'`'。'

*global.css*
```css
@import "tailwindcss";
```

#### 步骤 5: 开始您的构建过程

'使'用'`'n'p'm' 'r'u'n' 'd'e'v'运'行'`'构'建'过'程'。'

*Terminal*
```shell
npm run dev
```

#### 步骤 6: 开始在您的项目中使用 Tailwind

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

### <a id="react-router"></a>使用 React Router 安装 Tailwind CSS

在 React Router 项目中设置 Tailwind CSS。

#### 步骤 1: 创建您的项目

'S't'a'r't' 'b'y' 'c'r'e'a't'i'n'g' 'a' 'n'e'w' 'R'e'a'c't' 'R'o'u't'e'r' 'p'r'o'j'e'c't' 'i'f' 'y'o'u' 'd'o'n'''t' 'h'a'v'e' 'o'n'e' 's'e't' 'u'p' 'a'l'r'e'a'd'y'.' 'T'h'e' 'm'o's't' 'c'o'm'm'o'n' 'a'p'p'r'o'a'c'h' 'i's' 't'o' 'u's'e' '['C'r'e'a't'e' 'R'e'a'c't' 'R'o'u't'e'r']'('h't't'p's':'/'/'r'e'a'c't'r'o'u't'e'r'.'c'o'm'/'s't'a'r't'/'f'r'a'm'e'w'o'r'k'/'i'n's't'a'l'l'a't'i'o'n')'.'

*Terminal*
```shell
npx create-react-router@latest my-project
        cd my-project
```

#### 步骤 2: 安装 Tailwind CSS

'通'过'n'p'm'`'安'装'@'t'a'i'l'w'i'n'd'c's's'/'v'i't'e'`'及'其'对'等'依'赖'。'

*Terminal*
```shell
npm install tailwindcss @tailwindcss/vite
```

#### 步骤 3: 配置Vite插件

'将'`'@'t'a'i'l'w'i'n'd'c's's'/'v'i't'e'`'插'件'添'加'到'您'的'V'i't'e'配'置'中'。'

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

#### 步骤 4: 导入 Tailwind CSS

'将'`'@' 'i'm'p'o'r't'添'加'到'导'入'`'顺'风'C'S'S'的'`'.'/'a'p'p'/'a'p'p'.'c's's'`'。'

*app.css*
```css
@import "tailwindcss";
```

#### 步骤 5: 开始您的构建过程

'使'用'`'n'p'm' 'r'u'n' 'd'e'v'运'行'`'构'建'过'程'。'

*Terminal*
```shell
npm run dev
```

#### 步骤 6: 开始在您的项目中使用 Tailwind

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

### <a id="rspack"></a>使用 Rspack 安装 Tailwind CSS

在 Rspack 项目中设置 Tailwind CSS。

#### 步骤 1: 创建您的项目

'S't'a'r't' 'b'y' 'c'r'e'a't'i'n'g' 'a' 'n'e'w' 'R's'p'a'c'k' 'p'r'o'j'e'c't' 'i'f' 'y'o'u' 'd'o'n'''t' 'h'a'v'e' 'o'n'e' 's'e't' 'u'p' 'a'l'r'e'a'd'y'.' 'T'h'e' 'm'o's't' 'c'o'm'm'o'n' 'a'p'p'r'o'a'c'h' 'i's' 't'o' 'u's'e' '['R's'p'a'c'k' 'C'L'I']'('h't't'p's':'/'/'r's'p'a'c'k'.'d'e'v'/'g'u'i'd'e'/'s't'a'r't'/'q'u'i'c'k'-'s't'a'r't'#'u's'i'n'g'-'t'h'e'-'r's'p'a'c'k'-'c'l'i')'.'

*Terminal*
```shell
npm create rspack@latest
```

#### 步骤 2: 安装 Tailwind CSS

'安'装'`'@'t'a'i'l'w'i'n'd'c's's'/'p'o's't'c's's'`'及'其'对'等'依'赖'。'

*Terminal*
```shell
npm install tailwindcss @tailwindcss/postcss postcss postcss-loader
```

#### 步骤 3: 启用 PostCSS 支持

'在'r's'p'a'c'k'.'c'o'n'f'i'g'.'j's'`'文'件'`'中'，'启'用'P'o's't'C'S'S'加'载'器'。'有'关'更'多'信'['息'，'请'参'阅'文'档']'('h't't'p's':'/'/'r's'p'a'c'k'.'d'e'v'/'g'u'i'd'e'/'t'e'c'h'/'c's's'#'t'a'i'l'w'i'n'd'-'c's's')'。'

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

#### 步骤 4: 配置 PostCSS 插件

'在'项'目'根'`'目'`'录'中'创'建'p'o's't'c's's'.'c'o'n'f'i'g'.'m'j's'文'件'，'并'将'`'@'t'a'i'l'w'i'n'd'c's's'/'p'o's't'c's's'`'插'件'添'加'到'P'o's't'C'S'S'配'置'中'。'

*postcss.config.mjs*
```js
export default {
          plugins: {
            // [!code highlight:2]
            "@tailwindcss/postcss": {},
          },
        };
```

#### 步骤 5: 导入 Tailwind CSS

'将'`'@' 'i'm'p'o'r't'添'加'到'导'入'`'顺'风'C'S'S'的'`'.'/'s'r'c'/'i'n'd'e'x'.'c's's'`'。'

*index.css*
```css
@import "tailwindcss";
```

#### 步骤 6: 导入 Tailwind CSS

'将'`'@' 'i'm'p'o'r't'添'加'到'导'入'`'顺'风'C'S'S'的'`'.'/'s'r'c'/'s't'y'l'e'.'c's's'`'。'

*style.css*
```css
@import "tailwindcss";
```

#### 步骤 7: 开始您的构建过程

'使'用'`'n'p'm' 'r'u'n' 'd'e'v'运'行'`'构'建'过'程'。'

*Terminal*
```shell
npm run dev
```

#### 步骤 8: 开始在您的项目中使用 Tailwind

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

#### 步骤 9: 开始在您的项目中使用 Tailwind

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

### <a id="ruby-on-rails"></a>使用 Ruby on Rails 安装 Tailwind CSS

在 Ruby on Rails v8+ 项目中设置 Tailwind CSS。

#### 步骤 1: 创建您的项目

'S't'a'r't' 'b'y' 'c'r'e'a't'i'n'g' 'a' 'n'e'w' 'R'a'i'l's' 'p'r'o'j'e'c't' 'i'f' 'y'o'u' 'd'o'n'''t' 'h'a'v'e' 'o'n'e' 's'e't' 'u'p' 'a'l'r'e'a'd'y'.' 'T'h'e' 'm'o's't' 'c'o'm'm'o'n' 'a'p'p'r'o'a'c'h' 'i's' 't'o' 'u's'e' 't'h'e' '['R'a'i'l's' 'C'o'm'm'a'n'd' 'L'i'n'e']'('h't't'p's':'/'/'g'u'i'd'e's'.'r'u'b'y'o'n'r'a'i'l's'.'o'r'g'/'c'o'm'm'a'n'd'_'l'i'n'e'.'h't'm'l')'.'

*Terminal*
```shell
rails new my-project
        cd my-project
```

#### 步骤 2: 安装 Tailwind CSS

'安'装'`'t'a'i'l'w'i'n'd'c's's'-'r'a'i'l's'`' 'g'e'm' '，'然'后'运'行'i'n's't'a'l'l'命'令'在'项'目'中'设'置'T'a'i'l'w'i'n'd' 'C'S'S'。'

*Terminal*
```shell
bundle add tailwindcss-rails
        ./bin/rails tailwindcss:install
```

#### 步骤 3: 开始您的构建过程

'使'用'`'.'/'b'i'n'/'d'e'v'`'运'行'构'建'过'程'。'

*Terminal*
```shell
./bin/dev
```

#### 步骤 4: 开始在您的项目中使用 Tailwind

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

### <a id="solidjs"></a>使用 SolidJS 安装 Tailwind CSS

在 SolidJS 项目中设置 Tailwind CSS。

#### 步骤 1: 创建您的项目

'S't'a'r't' 'b'y' 'c'r'e'a't'i'n'g' 'a' 'n'e'w' 'S'o'l'i'd'J'S' 'p'r'o'j'e'c't' 'i'f' 'y'o'u' 'd'o'n'''t' 'h'a'v'e' 'o'n'e' 's'e't' 'u'p' 'a'l'r'e'a'd'y'.' 'T'h'e' 'm'o's't' 'c'o'm'm'o'n' 'a'p'p'r'o'a'c'h' 'i's' 't'o' 'u's'e' '['t'h'e' 'S'o'l'i'd'J'S' 'V'i't'e' 't'e'm'p'l'a't'e']'('h't't'p's':'/'/'w'w'w'.'s'o'l'i'd'j's'.'c'o'm'/'g'u'i'd'e's'/'g'e't't'i'n'g'-'s't'a'r't'e'd')'.'

*Terminal*
```shell
npx degit solidjs/templates/js my-project
        cd my-project
```

#### 步骤 2: 安装 Tailwind CSS

'通'过'n'p'm'`'安'装'@'t'a'i'l'w'i'n'd'c's's'/'v'i't'e'`'及'其'对'等'依'赖'。'

*Terminal*
```shell
npm install tailwindcss @tailwindcss/vite
```

#### 步骤 3: 配置Vite插件

'将'`'@'t'a'i'l'w'i'n'd'c's's'/'v'i't'e'`'插'件'添'加'到'您'的'V'i't'e'配'置'中'。'

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

#### 步骤 4: 导入 Tailwind CSS

'将'`'@' 'i'm'p'o'r't'添'加'到'导'入'`'顺'风'C'S'S'的'`'.'/'s'r'c'/'i'n'd'e'x'.'c's's'`'。'

*index.css*
```css
@import "tailwindcss";
```

#### 步骤 5: 开始您的构建过程

'使'用'`'n'p'm' 'r'u'n' 'd'e'v'运'行'`'构'建'过'程'。'

*Terminal*
```shell
npm run dev
```

#### 步骤 6: 开始在您的项目中使用 Tailwind

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

### <a id="sveltekit"></a>使用 SvelteKit 安装 Tailwind CSS

在 SvelteKit 项目中设置 Tailwind CSS。

#### 步骤 1: 创建您的项目

'S't'a'r't' 'b'y' 'c'r'e'a't'i'n'g' 'a' 'n'e'w' 'S'v'e'l't'e'K'i't' 'p'r'o'j'e'c't' 'i'f' 'y'o'u' 'd'o'n'''t' 'h'a'v'e' 'o'n'e' 's'e't' 'u'p' 'a'l'r'e'a'd'y'.' 'T'h'e' 'm'o's't' 'c'o'm'm'o'n' 'a'p'p'r'o'a'c'h' 'i's' 'o'u't'l'i'n'e'd' 'i'n' 't'h'e' '['S'v'e'l't'e'K'i't']'('h't't'p's':'/'/'s'v'e'l't'e'.'d'e'v'/'d'o'c's'/'k'i't'/'c'r'e'a't'i'n'g'-'a'-'p'r'o'j'e'c't')' 'd'o'c'u'm'e'n't'a't'i'o'n'.'

*Terminal*
```shell
npx sv create my-project
        cd my-project
```

#### 步骤 2: 安装 Tailwind CSS

'通'过'n'p'm'`'安'装'@'t'a'i'l'w'i'n'd'c's's'/'v'i't'e'`'及'其'对'等'依'赖'。'

*Terminal*
```shell
npm install tailwindcss @tailwindcss/vite
```

#### 步骤 3: 配置Vite插件

'将'`'@'t'a'i'l'w'i'n'd'c's's'/'v'i't'e'`'插'件'添'加'到'您'的'V'i't'e'配'置'中'。'

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

#### 步骤 4: 导入 Tailwind CSS

'创'建'`'.'/'s'r'c'/'a'p'p'.'c's's'`'文'件'并'添'加'导'入'顺'风'C'S'S'的'`'@' 'i'm'p'o'r't'`'。'

*app.css*
```css
@import "tailwindcss";
```

#### 步骤 5: 导入 CSS 文件

'创'建'`'.'/'s'r'c'/'r'o'u't'e's'/'+'l'a'y'o'u't'.'s'v'e'l't'e'文'件'并'`'导'入'新'创'建'的'`'a'p'p'.'c's's'`'文'件'。'

*+layout.svelte*
```svelte
<script>
          let { children } = $props();
          // [!code highlight:2]
          import "../app.css";
        </script>

        {@render children()}
```

#### 步骤 6: 开始您的构建过程

'使'用'`'n'p'm' 'r'u'n' 'd'e'v'运'行'`'构'建'过'程'。'

*Terminal*
```shell
npm run dev
```

#### 步骤 7: 开始在您的项目中使用 Tailwind

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

### <a id="symfony"></a>使用 Symfony 安装 Tailwind CSS

在 Symfony 项目中设置 Tailwind CSS。

#### 步骤 1: 创建您的项目

'S't'a'r't' 'b'y' 'c'r'e'a't'i'n'g' 'a' 'n'e'w' 'S'y'm'f'o'n'y' 'p'r'o'j'e'c't' 'i'f' 'y'o'u' 'd'o'n'''t' 'h'a'v'e' 'o'n'e' 's'e't' 'u'p' 'a'l'r'e'a'd'y'.' 'T'h'e' 'm'o's't' 'c'o'm'm'o'n' 'a'p'p'r'o'a'c'h' 'i's' 't'o' 'u's'e' '['t'h'e' 'S'y'm'f'o'n'y' 'I'n's't'a'l'l'e'r']'('h't't'p's':'/'/'s'y'm'f'o'n'y'.'c'o'm'/'d'o'w'n'l'o'a'd')'.'

*Terminal*
```shell
symfony new --webapp my-project
        cd my-project
```

#### 步骤 2: 安装 Webpack Encore

'安'装'W'e'b'p'a'c'k' 'E'n'c'o'r'e' '，'它'负'责'构'建'您'的'资'产'。'有'关'更'多'信'['息'，'请'参'阅'文'档']'('h't't'p's':'/'/'s'y'm'f'o'n'y'.'c'o'm'/'d'o'c'/'c'u'r'r'e'n't'/'f'r'o'n't'e'n'd'.'h't'm'l')'。'

*Terminal*
```shell
composer remove symfony/ux-turbo symfony/asset-mapper symfony/stimulus-bundle
        composer require symfony/webpack-encore-bundle symfony/ux-turbo symfony/stimulus-bundle
```

#### 步骤 3: 安装 Tailwind CSS

'U's'i'n'g' 'n'p'm',' 'i'n's't'a'l'l' '`'@'t'a'i'l'w'i'n'd'c's's'/'p'o's't'c's's'`' 'a'n'd' 'i't's' 'p'e'e'r' 'd'e'p'e'n'd'e'n'c'i'e's',' 'a's' 'w'e'l'l' 'a's' '`'p'o's't'c's's'-'l'o'a'd'e'r'`'.'

*Terminal*
```shell
npm install tailwindcss @tailwindcss/postcss postcss postcss-loader
```

#### 步骤 4: 启用 PostCSS 支持

'在'`'w'e'b'p'a'c'k'.'c'o'n'f'i'g'.'j's'`'文'件'中'，'启'用'P'o's't'C'S'S'加'载'器'。'有'关'更'多'信'['息'，'请'参'阅'文'档']'('h't't'p's':'/'/'s'y'm'f'o'n'y'.'c'o'm'/'d'o'c'/'c'u'r'r'e'n't'/'f'r'o'n't'e'n'd'/'e'n'c'o'r'e'/'p'o's't'c's's'.'h't'm'l')'。'

*webpack.config.js*
```js
Encore
          .enablePostCssLoader()
        ;
```

#### 步骤 5: 配置 PostCSS 插件

'在'项'目'根'`'目'`'录'中'创'建'p'o's't'c's's'.'c'o'n'f'i'g'.'m'j's'文'件'，'并'将'`'@'t'a'i'l'w'i'n'd'c's's'/'p'o's't'c's's'`'插'件'添'加'到'P'o's't'C'S'S'配'置'中'。'

*postcss.config.mjs*
```js
export default {
          plugins: {
            // [!code highlight:2]
            "@tailwindcss/postcss": {},
          },
        };
```

#### 步骤 6: 导入 Tailwind CSS

'向'`'.'/'a's's'e't's'/'s't'y'l'e's'/'a'p'p'.'c's's'`'添'加'导'入'顺'风'C'S'S'的'`'@' 'i'm'p'o'r't'`'和'忽'略'公'共'目'录'以'防'止'在'监'视'模'式'下'重'新'编'译'循'环'的'`'@' 's'o'u'r'c'e'`'。'

*app.css*
```css
@import "tailwindcss";
        @source not "../../public";
```

#### 步骤 7: 开始您的构建过程

'使'用'`'n'p'm' 'r'u'n' 'w'a't'c'h'运'行'`'构'建'过'程'。'

*Terminal*
```shell
npm run watch
```

#### 步骤 8: 开始在您的项目中使用 Tailwind

'确'保'已'编'译'的'C'S'S'包'含'在'中'，'`'<'h'e'a'd'>'`'然'后'开'始'使'用'T'a'i'l'w'i'n'd'的'实'用'程'序'类'来'设'置'内'容'的'样'式'。'

---

### <a id="tanstack-start"></a>使用 TanStack Start 安装 Tailwind CSS

在 TanStack Start 项目中设置 Tailwind CSS。

#### 步骤 1: 创建项目

'S't'a'r't' 'b'y' 'c'r'e'a't'i'n'g' 'a' 'n'e'w' 'T'a'n'S't'a'c'k' 'S't'a'r't' 'p'r'o'j'e'c't' 'i'f' 'y'o'u' 'd'o'n'''t' 'h'a'v'e' 'o'n'e' 's'e't' 'u'p' 'a'l'r'e'a'd'y'.' 'T'h'e' 'm'o's't' 'c'o'm'm'o'n' 'a'p'p'r'o'a'c'h' 'i's' 't'o' 'u's'e' '['C'r'e'a't'e' 'S't'a'r't' 'A'p'p']'('h't't'p's':'/'/'t'a'n's't'a'c'k'.'c'o'm'/'s't'a'r't'/'l'a't'e's't'/'d'o'c's'/'f'r'a'm'e'w'o'r'k'/'r'e'a'c't'/'o'v'e'r'v'i'e'w')'.'

*Terminal*
```shell
npx create-start-app@latest my-project
        cd my-project
```

#### 步骤 2: 安装 Tailwind CSS

'通'过'n'p'm'`'安'装'@'t'a'i'l'w'i'n'd'c's's'/'v'i't'e'`'及'其'对'等'依'赖'。'

*Terminal*
```shell
npm install tailwindcss @tailwindcss/vite
```

#### 步骤 3: 配置Vite插件

'将'`'@'t'a'i'l'w'i'n'd'c's's'/'v'i't'e'`'插'件'添'加'到'您'的'V'i't'e'配'置'中'。'

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

#### 步骤 4: 导入 Tailwind CSS

'将'导'入'顺'风'C'S'S'的'`'@' 'i'm'p'o'r't'`'添'加'到'`'.'/'s'r'c'/'s't'y'l'e's'.'c's's'`'。'

*src/styles.css*
```css
@import "tailwindcss";
```

#### 步骤 5: 在根路由中导入 CSS 文件

'使'用'`'?' 'u'r'l'`'查'询'将'`'C'S'S'`'文'件'导'入'_'_'r'o'o't'.'t's'x'文'件'中'。'

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

#### 步骤 6: 开始在您的项目中使用 Tailwind

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

