"""Tests for curated portfolio content."""

from pathlib import Path

from content import SITE_CONTENT


def test_nav_uses_portfolio_label():
    """Navigation should expose a portfolio label instead of projects."""
    labels = [item["label"] for item in SITE_CONTENT["nav_items"]]
    assert "Portfolio" in labels
    assert "Projects" not in labels


def test_portfolio_cases_have_required_fields():
    """Every portfolio case should be renderable by the template."""
    required_keys = {
        "slug",
        "title",
        "organization",
        "period",
        "logo",
        "summary",
        "approach",
        "impact",
        "stack",
        "preview_metric",
        "preview_support",
    }

    for case in SITE_CONTENT["portfolio_cases"]:
        assert required_keys.issubset(case.keys())
        assert case["approach"]
        assert case["impact"]
        assert case["stack"]


def test_resume_asset_exists():
    """The downloadable resume asset should exist under static/."""
    project_root = Path(__file__).resolve().parent
    resume_path = project_root / "static" / SITE_CONTENT["profile"]["resume_asset"]
    assert resume_path.exists()


def test_logo_assets_exist():
    """Brand wall assets referenced by content should exist."""
    project_root = Path(__file__).resolve().parent

    for logo in SITE_CONTENT["brand_logos"]:
        logo_path = project_root / "static" / logo["filename"]
        assert logo_path.exists()
        assert logo["tier"] in {"primary", "secondary"}


def test_logo_tiers_include_primary_and_secondary():
    """The brand wall should differentiate hero brands from supporting marks."""
    tiers = {logo["tier"] for logo in SITE_CONTENT["brand_logos"]}
    assert tiers == {"primary", "secondary"}


def test_resume_sync_preserves_philips_and_adds_cloud_project():
    """Resume-backed content should retain Philips and include the cloud strategy project."""
    companies = {entry["company"] for entry in SITE_CONTENT["experience_entries"]}
    project_titles = {project["title"] for project in SITE_CONTENT["academic_projects"]}
    case_titles = {case["title"] for case in SITE_CONTENT["portfolio_cases"]}

    assert "Philips Healthcare" in companies
    assert "Cloud Migration & Multi-Cloud Integration Strategy" in project_titles
    assert "Cloud Migration & Multi-Cloud Integration Strategy" in case_titles
