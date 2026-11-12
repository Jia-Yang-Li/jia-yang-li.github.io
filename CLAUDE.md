# Jiayang Li's personal website

Bilingual (English and Chinese) academic homepage built on the al-folio v1.x Jekyll starter. The site is served from the repository root of `jia-yang-li.github.io`, so `baseurl` in `_config.yml` stays empty.

## Who edits what

The owner edits content through Pages CMS (app.pagescms.org), which commits straight to `main` and so publishes. The forms are defined in `.pages.yml`. Design and structure changes are made here.

Because the owner commits to `main` from the CMS, run `git pull` on `main` and merge it into `preview` before editing anything.

`使用说明.md` is the owner's guide to the CMS. Update it when a form changes.

## Content

All page content is in `_data/`, with one field per language (`*_en`, `*_zh`):

- `profile.yml` — name, photo, subtitle, biography, contact links.
- `publications.yml` — the publication list. `bin/build_bib.py` turns it into `_bibliography/papers.bib` during the build; that file is generated and git-ignored. A publication's `image` (stored under `assets/img/publication_preview/`) becomes the theme's `preview` thumbnail.
- `news.yml` — news items for the home page, shown by month. The news section and its menu link are hidden while the list is empty.
- `cv_content.yml` — education, experience, projects, skills.
- `i18n.yml` — interface text per language (section headings, the language switch label).

When a field is added to a data file, add it to `.pages.yml` too. Pages CMS rewrites a file from its form schema, so a key missing from the schema is dropped on the next save.

Papers under review show only "Under review", never the venue. A paper at a double-blind venue stays off the site until it is accepted or public on arXiv.

Keep the phone number, age and other personal details from the Chinese CV in the parent folder off the site.

## Pages and languages

English pages are at `/` and `/cv/`; Chinese pages at `/zh/` and `/zh/cv/`. The home page holds the biography, research-interest tags, news and the full publication list; the menu links to its `#news` and `#publications` sections. Each page in `_pages/` sets `lang: en` or `lang: zh`. A Chinese page's URL is the English one prefixed with `/zh`; the header relies on this to link the two.

Local overrides of the theme:

- `_includes/header.liquid` — menu limited to the current language, plus the language switch.
- `_layouts/home.liquid` — home page rendered from `profile.yml`, `news.yml` and the generated bibliography.
- `_layouts/cv_bilingual.liquid` and `_includes/cv_entry.liquid` — CV page rendered from `cv_content.yml`.

Everything else (layouts, includes, Sass, Liquid tags) comes from the `al_folio_*` gems pinned in `Gemfile`. `Gemfile` and the `plugins:` list in `_config.yml` must agree. A feature that is switched off renders nothing and gives no error. Theme documentation is in `docs/`; the gem sources are at github.com/al-org-dev.

In Liquid, test for an empty value with `x and x != ''`. `x != blank` is true for an empty string here.

The theme sets `float: left !important` on `.float-left`, so page-level CSS cannot turn the profile photo's float off.

## Build and deploy

There is no local Ruby or Docker on the Windows machine, so the site is not built locally.

Work on the `preview` branch. A push to `preview` runs `.github/workflows/preview.yml`, which builds the site into the `preview-site` branch and publishes nothing. To view it locally:

```bash
git fetch origin preview-site
git archive FETCH_HEAD | tar -x -C "$LOCALAPPDATA/jia-yang-li-preview"
python -m http.server 4000 --bind 127.0.0.1 --directory "$LOCALAPPDATA/jia-yang-li-preview"
```

The `site-preview` entry in `../.claude/launch.json` starts the same server.

A push to `main` runs `.github/workflows/deploy.yml`, which builds and publishes to the `gh-pages` branch that GitHub Pages serves. Push design changes to `main` only after the owner has approved the preview. Check the Actions run and the live site after each push.
