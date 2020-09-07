from flask import Flask, url_for
app = Flask(__name__)


@app.route("/home")
@app.route("/")
def home():
    return "<h1>Home Page<h1>"


@app.route("/about")
def about():
    return "<h1>About Page<h1>"

if __name__ == '__main__':
    app.run(debug=True)