from flask import Flask, render_template, redirect, request
from flask_login import LoginManager, login_user, login_required, logout_user
from shutil import copy

from data import db_session
from data.login_form import LoginForm
from data.users import User
from data.games import Games
from data.register import RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route("/profile")
def profile():
    return render_template("profile.html", title='Профиль')


@app.route("/profile/change", methods=['POST', 'GET'])
def change():
    if request.method == 'POST':
        f = request.files['file']
        id = request.form.get('id')
        # id = request.form.get('id')
        with open(f'static/img/avatar/{id}.jpg', 'wb') as file:
            file.write(f.read())
        # return render_template("profile.html", title='Профиль')
    return render_template("change.html", title='Профиль')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html', message="Неверный пароль или логин", form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/hab')
@app.route('/')
def hab():
    return render_template("hab.html", title='НУАР')


@app.route('/search')
def search():
    db_sess = db_session.create_session()
    games = db_sess.query(Games).all()
    return render_template("search.html", title='Поиск игры', games=games)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация', form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация', form=form,
                                   message="Этот пользователь уже существует")
        user = User(
            surname=form.surname.data,
            email=form.email.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        copy("static/img/avatar/photo.jpg", f'static/img/avatar/{user.id}.jpg')
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


def main():
    db_session.global_init("db/mars_explorer.sqlite")
    app.run(host='0.0.0.0', port=8080, debug=True)


if __name__ == '__main__':
    main()


