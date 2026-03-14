"""Export the Flask portfolio into a static site for Cloudflare Pages."""

from __future__ import annotations

import os
import shutil
from pathlib import Path

from flask import render_template

from app import app, build_page

PROJECT_ROOT = Path(__file__).resolve().parent
DEFAULT_OUTPUT_DIR = PROJECT_ROOT / "dist"
STATIC_DIR = PROJECT_ROOT / "static"
DEFAULT_SITE_URL = "http://localhost:8001"

EXPORT_ROUTES = (
    ("/", "index.html", 200),
    ("/about/", "about/index.html", 200),
    ("/resume/", "resume/index.html", 200),
    ("/projects/", "projects/index.html", 200),
    ("/contact/", "contact/index.html", 200),
    ("/missing-page-for-export", "404.html", 404),
)

REDIRECTS_CONTENT = """/about /about/ 308
/resume /resume/ 308
/projects /projects/ 308
/contact /contact/ 308
/thankyou /contact/ 308
"""

HEADERS_CONTENT = """/*
  X-Content-Type-Options: nosniff
  X-Frame-Options: DENY
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: accelerometer=(), camera=(), geolocation=(), gyroscope=(), microphone=(), payment=(), usb=()
  Content-Security-Policy: default-src 'self'; img-src 'self' data: https:; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com; script-src 'self' 'unsafe-inline'; connect-src 'self'; object-src 'none'; base-uri 'self'; form-action 'self'; frame-ancestors 'none'; upgrade-insecure-requests

/static/css/*
  Cache-Control: public, max-age=31536000, immutable

/static/js/*
  Cache-Control: public, max-age=31536000, immutable

/static/images/*
  Cache-Control: public, max-age=31536000, immutable

/static/resume/*
  Cache-Control: public, max-age=3600
"""


def write_text_file(path: Path, content: str) -> None:
    """Write UTF-8 text content, creating parent directories as needed."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def export_rendered_pages(output_dir: Path, site_url: str) -> None:
    """Render all public routes through the Flask app and write them to disk."""
    client = app.test_client()

    for route_path, output_path, expected_status in EXPORT_ROUTES:
        response = client.get(route_path, base_url=site_url)
        if response.status_code != expected_status:
            raise RuntimeError(
                f"Expected {expected_status} for {route_path}, got {response.status_code}"
            )

        destination = output_dir / output_path
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(response.get_data(as_text=True), encoding="utf-8")


def export_static_error_page(output_dir: Path, site_url: str) -> None:
    """Render the informational 500 page for completeness in local previews."""
    with app.test_request_context("/500/", base_url=site_url):
        html = render_template(
            "500.html",
            **build_page(
                "Server Error | Aneesh Yaramati",
                "The portfolio hit an unexpected issue.",
                "",
                "page-error",
            ),
        )

    write_text_file(output_dir / "500.html", html)


def build_static_site(output_dir: Path | None = None, site_url: str | None = None) -> Path:
    """Create the static export directory used by Cloudflare Pages."""
    destination = output_dir or DEFAULT_OUTPUT_DIR
    public_site_url = (site_url or DEFAULT_SITE_URL).rstrip("/")

    if destination.exists():
        shutil.rmtree(destination)

    destination.mkdir(parents=True, exist_ok=True)
    export_rendered_pages(destination, public_site_url)
    export_static_error_page(destination, public_site_url)
    shutil.copytree(STATIC_DIR, destination / "static", dirs_exist_ok=True)
    write_text_file(destination / "_redirects", REDIRECTS_CONTENT)
    write_text_file(destination / "_headers", HEADERS_CONTENT)
    return destination


def main() -> None:
    """CLI entrypoint used by local builds and Cloudflare Pages."""
    destination = build_static_site(site_url=os.environ.get("SITE_URL", DEFAULT_SITE_URL))
    print(f"Static site exported to {destination}")


if __name__ == "__main__":
    main()
