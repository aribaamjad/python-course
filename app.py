from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Railway"

@app.route("/test")
def test():
    return "Website is working!"
