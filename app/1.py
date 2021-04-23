from flask import Flask, render_template, redirect

app = Flask(__name__)



@app.route("/")
def base():
    return render_template("base.html", titel='ХАБ')


# @app.route("/navi")
# def navi():
#     return render_template("index.html")


def main():
    app.run(host='0.0.0.0', port=8080, debug=True)


if __name__ == '__main__':
    main()
