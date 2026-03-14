"""Route tests for the recruiting-first portfolio website."""

import datetime


class TestPublicRoutes:
    """Test the retained public routes."""

    def test_index_route(self, client):
        response = client.get("/")
        assert response.status_code == 200
        assert b"Recruiting-first portfolio" in response.data
        assert b"Data Engineer + MSIS @ Kelley" in response.data

    def test_about_route(self, client):
        response = client.get("/about")
        assert response.status_code == 200
        assert b"About the portfolio" in response.data

    def test_resume_route(self, client):
        response = client.get("/resume")
        assert response.status_code == 200
        assert b"Resume-aligned view" in response.data
        assert b"Download PDF" in response.data

    def test_portfolio_route(self, client):
        response = client.get("/projects")
        assert response.status_code == 200
        assert b"Portfolio" in response.data
        assert b"TMHNA Digital Momentum" in response.data
        assert b"SLB Enterprise Data Engineering" in response.data
        assert b"Cloud Migration &amp; Multi-Cloud Integration Strategy" in response.data

    def test_contact_route(self, client):
        response = client.get("/contact")
        assert response.status_code == 200
        assert b"Make the next step easy" in response.data
        assert b"LinkedIn" in response.data
        assert b"Resume" in response.data

    def test_contact_route_post_not_allowed(self, client):
        response = client.post("/contact")
        assert response.status_code == 405


class TestRemovedRoutes:
    """Ensure the old assignment CRUD surface is gone."""

    def test_add_project_removed_get(self, client):
        response = client.get("/add_project")
        assert response.status_code == 404

    def test_add_project_removed_post(self, client):
        response = client.post("/add_project")
        assert response.status_code == 404

    def test_delete_project_removed(self, client):
        response = client.post("/delete_project/1")
        assert response.status_code == 404


class TestRedirectsAndErrors:
    """Test legacy redirects and error handling."""

    def test_thankyou_redirects_to_contact(self, client):
        response = client.get("/thankyou")
        assert response.status_code == 302
        assert response.headers["Location"].endswith("/contact")

    def test_404_handler(self, client):
        response = client.get("/missing-page")
        assert response.status_code == 404
        assert b"That page is not in the portfolio" in response.data


class TestTemplateContent:
    """Test key rendered content and shared layout behavior."""

    def test_current_year_in_footer(self, client):
        response = client.get("/")
        current_year = str(datetime.datetime.now().year)
        assert current_year.encode() in response.data

    def test_navigation_uses_portfolio_label(self, client):
        response = client.get("/")
        assert b"Portfolio" in response.data
        assert b">Projects<" not in response.data

    def test_resume_download_uses_pdf_asset(self, client):
        response = client.get("/resume")
        assert b"Yaramati_Aneesh_Resume.pdf" in response.data

    def test_brand_logos_render_on_homepage(self, client):
        response = client.get("/")
        assert b"iu-kelley.svg" in response.data
        assert b"slb.svg" in response.data
        assert b"tmhna.svg" in response.data
        assert b"logo-card--primary" in response.data
        assert b"logo-card--secondary" in response.data

    def test_resume_page_keeps_philips_experience(self, client):
        response = client.get("/resume")
        assert b"Philips Healthcare" in response.data

    def test_layout_bootstraps_progressive_reveal(self, client):
        response = client.get("/")
        assert b'<html lang="en" class="no-js">' in response.data
        assert b'classList.add("js")' in response.data
