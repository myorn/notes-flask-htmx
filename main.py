from flask import Flask

app = Flask(__name__)


@app.route("/")
def serve_front_page():
    return "Whateve"
