from flask import Flask, render_template
import os

app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return render_template("index.html")

# AI Tools Page
@app.route("/tools")
def tools():
    return render_template("tools.html")

# About Page
@app.route("/about")
def about():
    return render_template("about.html")

# Contact Page
@app.route("/contact")
def contact():
    return render_template("contact.html")

# Privacy Policy Page
@app.route("/privacy")
def privacy():
    return render_template("privacy.html")
@app.route("/terms")
def terms():
    return render_template("terms.html")
@app.route("/disclaimer")
def disclaimer():
    return render_template("disclaimer.html")
@app.route("/blog")
def blog():
    return render_template("blog.html")
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=False)

