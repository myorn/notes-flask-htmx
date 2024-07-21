from flask import Flask

app = Flask(__name__)


@app.route("/")
def serve_front_page():
    return "Whateve"


@app.route("/records")
def get_records():
    return "Whateve"


@app.route("/record")
def post_record():
    return "Whateve"


@app.route("/record")
def edit_record():
    return "Whateve"


@app.route("/record")
def delete_record():
    return "Whateve"
