# Jiayang Li — personal website

Academic homepage built with the [al-folio](https://github.com/alshedivat/al-folio) Jekyll theme and hosted on GitHub Pages.

## Where the content lives

| What                     | File                         |
| ------------------------ | ---------------------------- |
| Home page biography      | `_pages/about.md`            |
| Publications             | `_bibliography/papers.bib`   |
| CV page                  | `_data/cv.yml`               |
| Email and social links   | `_data/socials.yml`          |
| Site name, URL, features | `_config.yml`                |
| Profile photo            | `assets/img/prof_pic.jpg`    |
| News items               | `_news/` (currently unused)  |

## Publishing

Pushing to the `main` branch runs `.github/workflows/deploy.yml`, which builds the site and publishes it to the `gh-pages` branch. GitHub Pages serves that branch.

Theme documentation is in `docs/`.
