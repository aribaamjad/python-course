from flask import Flask, render_template, request

app = Flask(__name__)

# =========================
# Home
# =========================
@app.route("/")
def home():
    return render_template("index.html")

# =========================
# AI Tools
# =========================
@app.route("/tools")
def tools():
    return render_template("tools.html")

# =========================
# About
# =========================
@app.route("/about")
def about():
    return render_template("about.html")

# =========================
# Contact
# =========================
@app.route("/contact", methods=["GET", "POST"])
def contact():

    success = False

    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        print("\n===== NEW MESSAGE =====")
        print("Name:", name)
        print("Email:", email)
        print("Message:", message)
        print("=======================\n")

        success = True

    return render_template("contact.html", success=success)

# =========================
# Login
# =========================
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        print("User Login Attempt")

    return render_template("login.html")

# =========================
# Signup
# =========================
@app.route("/signup", methods=["GET", "POST"])
def signup():

    if request.method == "POST":
        print("New User Signup")

    return render_template("signup.html")
@app.route("/terms")
def terms():
    return render_template("terms.html")


@app.route("/disclaimer")
def disclaimer():
    return render_template("disclaimer.html")


@app.route("/dmca")
def dmca():
    return render_template("dmca.html")
@app.route("/privacy")
def privacy():
    return render_template("privacy.html")
# =========================
# Run App
# =========================
if __name__ == "__main__":
    app.run(debug=True)

