# Aneesh Yaramati Portfolio

Recruiting-focused portfolio site built with Flask as the authoring layer and exported as a static site for Cloudflare Pages.

## Overview

- Source of truth: `content.py` + Jinja templates in `templates/`
- Local preview: Flask app in `app.py`
- Static deployment target: Cloudflare Pages
- Static export command: `python export_static.py`
- Static output directory: `dist/`

## Project Structure

```text
AiDD_Assignment07/
├── app.py
├── content.py
├── export_static.py
├── requirements.txt
├── static/
├── templates/
├── test_content.py
├── test_export_static.py
├── test_routes.py
└── README.md
```

## Local Development

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Flask preview server:

```bash
python app.py
```

Preview URLs:

- `http://127.0.0.1:8001/`
- `http://127.0.0.1:8001/about/`
- `http://127.0.0.1:8001/resume/`
- `http://127.0.0.1:8001/projects/`
- `http://127.0.0.1:8001/contact/`

The local preview accepts both `/about` and `/about/`, but the site generates trailing-slash URLs to match the static deployment.

## Static Export

Build the static site locally:

```bash
SITE_URL=https://your-project.pages.dev python export_static.py
```

This writes:

- `dist/index.html`
- `dist/about/index.html`
- `dist/resume/index.html`
- `dist/projects/index.html`
- `dist/contact/index.html`
- `dist/404.html`
- `dist/500.html`
- `dist/static/...`
- `dist/_redirects`
- `dist/_headers`

Preview the exported site locally:

```bash
python -m http.server 4173 --directory dist
```

Then open `http://127.0.0.1:4173`.

## Cloudflare Pages Deployment

Create a Cloudflare Pages project with Git integration using:

- Repository: `anyarama/Personal_website_docker`
- Production branch: `main`
- Root directory: `AiDD_Assignment07`
- Build command: `pip install -r requirements.txt && python export_static.py`
- Build output directory: `dist`

Set these build settings:

- Python version: `3.11`
- Environment variable: `SITE_URL=https://<your-project>.pages.dev`

After the first deploy, verify:

- `/`
- `/about/`
- `/resume/`
- `/projects/`
- `/contact/`
- `/thankyou` redirects to `/contact/`
- the resume PDF downloads from `/static/resume/Yaramati_Aneesh_Resume.pdf`

## Testing

Run the full test suite:

```bash
pytest -q
```

Static export coverage includes:

- generated HTML pages
- copied assets
- Cloudflare `_redirects`
- Cloudflare `_headers`
- canonical and Open Graph metadata
- resume PDF and logo availability
