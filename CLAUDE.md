# Jiayang Li's personal website

Academic homepage built on the al-folio v1.x Jekyll starter. The site is served from the repository root of `<username>.github.io`, so `baseurl` in `_config.yml` stays empty.

## Content

- `_pages/about.md` — home page biography and which home page blocks are on.
- `_bibliography/papers.bib` — publications. `selected = {true}` shows a paper on the home page. `abbr` values get their colour and link from `_data/venues.yml`.
- `_data/cv.yml` — CV page, RenderCV format.
- `_data/socials.yml` — email and social links.
- `assets/img/prof_pic.jpg` — profile photo.

Papers under review are `@article` entries with `journal = {Under review}` and no venue name. A paper submitted to a double-blind venue is left off the site until it is accepted or public on arXiv.

Keep the phone number, age and other personal details from the Chinese CV in the parent folder off the site.

## Theme

Layouts, includes, Sass and Liquid tags live in the `al_folio_*` gems pinned in `Gemfile`. `Gemfile` and the `plugins:` list in `_config.yml` must agree. A feature that is switched off renders nothing and gives no error. Theme documentation is in `docs/`.

Sample content from the template was deleted (blog, projects, news, books, teaching, repositories). To bring a section back, copy the page and collection from upstream al-folio.

## Build and deploy

There is no local Ruby or Docker on the Windows machine, so the site is not built locally.

Work on the `preview` branch. A push to `preview` runs `.github/workflows/preview.yml`, which builds the site into the `preview-site` branch and publishes nothing. To view it locally:

```bash
git fetch origin preview-site
rm -rf "$LOCALAPPDATA/jia-yang-li-preview" && mkdir -p "$LOCALAPPDATA/jia-yang-li-preview"
git archive FETCH_HEAD | tar -x -C "$LOCALAPPDATA/jia-yang-li-preview"
python -m http.server 4000 --bind 127.0.0.1 --directory "$LOCALAPPDATA/jia-yang-li-preview"
```

The `site-preview` entry in `../.claude/launch.json` starts the same server.

A push to `main` runs `.github/workflows/deploy.yml`, which builds and publishes to the `gh-pages` branch that GitHub Pages serves. Push to `main` only after the owner has approved the preview. Check the Actions run and the live site after each push.

The theme sets `float: left !important` on `.float-left`, so page-level CSS cannot turn the profile photo's float off.
