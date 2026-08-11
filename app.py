from flask import Flask, render_template
import os

app = Flask(__name__)


# ================= ROBOTS.TXT =================

@app.route("/robots.txt")
def robots():
    return """User-agent: *
Allow: /
Sitemap: https://python-course-qczt.vercel.app/sitemap.xml
""", 200, {"Content-Type": "text/plain"}


# ================= SITEMAP =================

@app.route("/sitemap.xml")
def sitemap():

    sitemap_xml = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">

    <url>
        <loc>https://python-course-qczt.vercel.app/</loc>
    </url>

    <url>
        <loc>https://python-course-qczt.vercel.app/tools</loc>
    </url>

    <url>
        <loc>https://python-course-qczt.vercel.app/about</loc>
    </url>

    <url>
        <loc>https://python-course-qczt.vercel.app/contact</loc>
    </url>

    <url>
        <loc>https://python-course-qczt.vercel.app/how-to-write-better-ai-prompts-2026.html</loc>
    </url>

    <url>
        <loc>https://python-course-qczt.vercel.app/top-10-free-ai-tools-2026.html</loc>
    </url>

    <url>
        <loc>https://python-course-qczt.vercel.app/top-10-free-ai-image-generators.html</loc>
    </url>

</urlset>
"""

    return sitemap_xml, 200, {"Content-Type": "application/xml"}


# ================= GOOGLE VERIFICATION =================

@app.route("/google853ead28f29bf53f.html")
def google_verification():
    return "google-site-verification: google853ead28f29bf53f.html"


# ================= HOME =================

@app.route("/")
def home():
    return render_template("index.html")


# ================= TOOLS =================

@app.route("/tools")
def tools():
    return render_template("tools.html")


# ================= ABOUT =================

@app.route("/about")
def about():
    return render_template("about.html")


# ================= CONTACT =================

@app.route("/contact")
def contact():
    return render_template("contact.html")


# ================= ARTICLE =================

@app.route("/how-to-write-better-ai-prompts-2026.html")
def ai_prompts_article():
    return render_template("how-to-write-better-ai-prompts-2026.html")


@app.route("/top-10-free-ai-tools-2026.html")
def free_ai_tools_article():
    return render_template("top-10-free-ai-tools-2026.html")


@app.route("/top-10-free-ai-image-generators.html")
def ai_image_generators_article():
    return render_template("top-10-free-ai-image-generators.html")


# ================= TEST =================

@app.route("/test")
def test():
    return "Website is working!"


# ================= RUN =================

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=False)