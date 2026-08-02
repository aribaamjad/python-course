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
@app.route("/blog/best-ai-tools-for-students")
def best_ai_tools_for_students():
    return render_template("best-ai-tools-for-students.html")
@app.route("/blog/top-10-free-ai-tools-2026")
def top_10_free_ai_tools_2026():
    return render_template("top-10-free-ai-tools-2026.html")
@app.route("/blog/chatgpt-beginner-guide")
def chatgpt_beginner_guide():
    return render_template("chatgpt-beginner-guide.html")
@app.route("/blog/top-10-free-ai-image-generators")
def top_10_free_ai_image_generators():
    return render_template("top-10-free-ai-image-generators.html")
@app.route("/blog/claude-vs-chatgpt-2026")
def claude_vs_chatgpt_2026():
    return render_template("claude-vs-chatgpt-2026.html")
@app.route("/blog/best-ai-tools-for-teachers-2026")
def best_ai_tools_for_teachers_2026():
    return render_template("best-ai-tools-for-teachers-2026.html")
@app.route("/blog/chatgpt-vs-gemini-2026")
def chatgpt_vs_gemini_2026():
    return render_template("chatgpt-vs-gemini-2026.html")
    @app.route("/blog/best-ai-resume-builders-2026")
def best_ai_resume_builders_2026():
    return render_template("best-ai-resume-builders-2026.html")
@app.route("/blog/best-free-ai-video-generators-2026")
def best_free_ai_video_generators_2026():
    return render_template("best-free-ai-video-generators-2026.html")
@app.route("/blog/how-to-write-better-ai-prompts-2026")
def how_to_write_better_ai_prompts_2026():
    return render_template("how-to-write-better-ai-prompts-2026.html")
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=False)

