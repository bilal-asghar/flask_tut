from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/<name>")
def harry(name):
    return f"<h2> I am {name}</h2>"


@app.route("/about")
def about():
    if request.method == "POST":
        name = request.form["name"]
        password = request.form["password"]
        # return f"<h2> I am {name} My password is {password}</h2>"
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True, port="5000", host="127.0.0.1")