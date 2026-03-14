# Personal Website Portfolio Repository

This repository contains Aneesh Yaramati's recruiting-focused portfolio site.

## Active Project

The live portfolio source is in `AiDD_Assignment07/`.

The current hosting model is:

- authoring layer: Flask + Jinja
- deployment target: static site on Cloudflare Pages
- static build command: `python export_static.py`

## Quick Start

```bash
cd AiDD_Assignment07
pip install -r requirements.txt
python app.py
```

Local preview:

- `http://127.0.0.1:8001/`
- `http://127.0.0.1:8001/about/`
- `http://127.0.0.1:8001/resume/`
- `http://127.0.0.1:8001/projects/`
- `http://127.0.0.1:8001/contact/`

## Static Export

```bash
cd AiDD_Assignment07
SITE_URL=https://your-project.pages.dev python export_static.py
python -m http.server 4173 --directory dist
```

## Deploy to Cloudflare Pages

Use these settings in Cloudflare Pages:

- Repository: `anyarama/Personal_website_docker`
- Branch: `main`
- Root directory: `AiDD_Assignment07`
- Build command: `pip install -r requirements.txt && python export_static.py`
- Build output directory: `dist`
- Environment variable: `SITE_URL=https://<your-project>.pages.dev`

Detailed project documentation is in `AiDD_Assignment07/README.md`.
