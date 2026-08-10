@app.route("/robots.txt")
def robots():
    return """User-agent: *
Allow: /
Sitemap: https://python-course-qczt.vercel.app/sitemap.xml
""", 200, {"Content-Type": "text/plain"}


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

</urlset>"""

    return sitemap_xml, 200, {"Content-Type": "application/xml"}