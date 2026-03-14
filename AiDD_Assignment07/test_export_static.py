"""Tests for the static export used by Cloudflare Pages."""

from export_static import build_static_site


def test_static_export_creates_expected_pages_and_assets(tmp_path):
    """The exporter should write all public pages, assets, and hosting files."""
    output_dir = build_static_site(
        output_dir=tmp_path / "dist",
        site_url="https://aneesh-portfolio.pages.dev",
    )

    expected_files = [
        output_dir / "index.html",
        output_dir / "about" / "index.html",
        output_dir / "resume" / "index.html",
        output_dir / "projects" / "index.html",
        output_dir / "contact" / "index.html",
        output_dir / "404.html",
        output_dir / "500.html",
        output_dir / "_redirects",
        output_dir / "_headers",
        output_dir / "static" / "resume" / "Yaramati_Aneesh_Resume.pdf",
        output_dir / "static" / "images" / "logos" / "philips.svg",
        output_dir / "static" / "css" / "styles.css",
        output_dir / "static" / "js" / "script.js",
    ]

    for expected_file in expected_files:
        assert expected_file.exists()


def test_static_export_preserves_core_content_and_absolute_metadata(tmp_path):
    """Exported HTML should keep core content and use the configured public origin."""
    output_dir = build_static_site(
        output_dir=tmp_path / "dist",
        site_url="https://aneesh-portfolio.pages.dev",
    )

    home_html = (output_dir / "index.html").read_text(encoding="utf-8")
    resume_html = (output_dir / "resume" / "index.html").read_text(encoding="utf-8")
    projects_html = (output_dir / "projects" / "index.html").read_text(encoding="utf-8")

    assert 'href="https://aneesh-portfolio.pages.dev/"' in home_html
    assert (
        'content="https://aneesh-portfolio.pages.dev/static/images/headshot.jpg"' in home_html
    )
    assert 'href="/projects/"' in home_html
    assert "SLB Enterprise Data Engineering" in projects_html
    assert "TMHNA Digital Momentum" in projects_html
    assert "Philips Healthcare" in resume_html
    assert "Yaramati_Aneesh_Resume.pdf" in resume_html


def test_static_export_writes_cloudflare_redirects_and_headers(tmp_path):
    """Cloudflare Pages support files should match the clean URL and caching plan."""
    output_dir = build_static_site(
        output_dir=tmp_path / "dist",
        site_url="https://aneesh-portfolio.pages.dev",
    )

    redirects = (output_dir / "_redirects").read_text(encoding="utf-8")
    headers = (output_dir / "_headers").read_text(encoding="utf-8")

    assert "/about /about/ 308" in redirects
    assert "/thankyou /contact/ 308" in redirects
    assert "X-Content-Type-Options: nosniff" in headers
    assert "Content-Security-Policy:" in headers
    assert "/static/images/*" in headers
    assert "/static/resume/*" in headers
