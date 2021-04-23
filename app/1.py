from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap

app = Flask(__name__)

# bootstrap = Bootstrap(app)


@app.route("/")
def base():
    return render_template("index2.html")


@app.route("/")
def navi():
    return render_template("index.html")


# @app.route("/")
# def df():
#     return render_template("index3.html")


def main():
    app.run(host='0.0.0.0', port=8080, debug=True)


if __name__ == '__main__':
    main()
