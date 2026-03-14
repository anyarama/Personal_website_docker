"""Flask entrypoint for the recruiting-focused portfolio site."""

import datetime
import os

from flask import Flask, redirect, render_template, url_for

from content import SITE_CONTENT

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get(
    "SECRET_KEY",
    "local-development-secret-key-change-me",
)


def build_page(title, description, active_page, body_class):
    """Shared page metadata passed to every public template."""
    return {
        "page_title": title,
        "page_description": description,
        "active_page": active_page,
        "body_class": body_class,
    }


@app.context_processor
def inject_globals():
    """Global template context used across the shared portfolio layout."""
    return {
        "current_year": datetime.datetime.now().year,
        "site": SITE_CONTENT,
        "resume_download_url": url_for("static", filename=SITE_CONTENT["profile"]["resume_asset"]),
    }


@app.route("/")
def index():
    """Portfolio landing page."""
    return render_template(
        "index.html",
        **build_page(
            "Aneesh Yaramati | Data Engineering Portfolio",
            "Recruiting-focused portfolio for enterprise data engineering, digital systems, and analytics-ready architecture.",
            "index",
            "page-home",
        ),
    )


@app.route("/about")
def about():
    """About page with story, education, and credibility context."""
    return render_template(
        "about.html",
        **build_page(
            "About | Aneesh Yaramati",
            "Background, education, and portfolio context for Aneesh Yaramati.",
            "about",
            "page-about",
        ),
    )


@app.route("/resume")
def resume():
    """Resume-aligned summary page."""
    return render_template(
        "resume.html",
        **build_page(
            "Resume | Aneesh Yaramati",
            "Resume-driven overview of experience, education, projects, and technical skills.",
            "resume",
            "page-resume",
        ),
    )


@app.route("/projects")
def projects():
    """Read-only portfolio page."""
    return render_template(
        "projects.html",
        **build_page(
            "Portfolio | Aneesh Yaramati",
            "Selected enterprise data, digital systems, and applied AI case studies.",
            "projects",
            "page-projects",
        ),
    )


@app.route("/contact")
def contact():
    """Recruiter CTA page."""
    return render_template(
        "contact.html",
        **build_page(
            "Contact | Aneesh Yaramati",
            "Direct recruiter-friendly contact options including email, LinkedIn, and resume download.",
            "contact",
            "page-contact",
        ),
    )


@app.route("/thankyou")
def thankyou():
    """Legacy thank-you route maintained as a redirect."""
    return redirect(url_for("contact"))


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 error page."""
    return (
        render_template(
            "404.html",
            **build_page(
                "Page Not Found | Aneesh Yaramati",
                "The page you requested could not be found.",
                "",
                "page-error",
            ),
        ),
        404,
    )


@app.errorhandler(500)
def internal_server_error(error):
    """Custom 500 error page."""
    return (
        render_template(
            "500.html",
            **build_page(
                "Server Error | Aneesh Yaramati",
                "The portfolio hit an unexpected issue.",
                "",
                "page-error",
            ),
        ),
        500,
    )


if __name__ == "__main__":
    app.run(
        debug=os.environ.get("FLASK_DEBUG", "").lower() in {"1", "true", "yes"},
        host="0.0.0.0",
        port=int(os.environ.get("PORT", "8001")),
    )
