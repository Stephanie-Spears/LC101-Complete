from flask import Flask, request, redirect, render_template, flash, session
import datetime
from app import app, db
from models import Blog, User
from hashutils import make_pw_hash, check_pw_hash


def check_username(username):
    error_username = ''

    if len(username) not in range(3, 51):
        error_username = 'Username must contain 3 - 50 characters'

    if ' ' in username:
        error_username = 'Username does not permit spaces'

    if '@' and '.' not in username:
        error_username = 'Username must contain @ and .'

    return error_username


def check_password(password, verify):
    error_password = ''

    if len(password) not in range(3, 21):
        error_password = 'Password must contain 3 - 20 characters'

    if len(verify) not in range(3, 21):
        error_password = 'Password must contain 3 - 20 characters'

    if password != verify:
        error_password = 'Passwords must match'

    return error_password


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password']
        verify = request.form['verify']

        error_username = check_username(username)
        error_password = check_password(password, verify)

        existing_user = User.query.filter_by(username=username).first()

        # no errors
        if not existing_user and all(x is '' for x in (error_username, error_password)):

            new_user = User(username, password)
            db.session.add(new_user)
            db.session.commit()
            session['username'] = username
            return redirect('/newpost')

        # errors
        if existing_user:
            flash('Username already exists', 'error_username')
            flash(error_password, 'error_password')

        # errors
        else:
            flash(error_username, 'error_username')
            flash(error_password, 'error_password')

        # provide state of attempted form
        return render_template('signup.html',
            title='signup',
            username=username,
            password=password,
            verify=verify)

    return render_template('signup.html',
        title='signup')


@app.route('/newpost', methods=['POST', 'GET'])
def newpost():

    post_title, post_body = '', ''
    owner = User.query.filter_by(username=session['username']).first()

    if request.method == 'POST':
        post_title = request.form['post_title']
        post_body = request.form['post_body']

        if post_title and post_body:
            new_post = Blog(post_title, post_body, owner)
            db.session.add(new_post)
            db.session.commit()

            post_id = str(new_post.id)
            return redirect('/blog?id=' + post_id)

        if not post_title:
            flash('Please fill in the title', 'error_title')

        if not post_body:
            flash('Please fill in the body', 'error_body')

    return render_template('newpost.html',
        title='newpost',
        post_title=post_title,
        post_body=post_body)


@app.route('/blog', methods=['POST', 'GET'])
def blog():

    post_id = request.args.get('id')
    user_id = request.args.get('user')

    if post_id:
        post = Blog.query.get(post_id)
        return render_template('viewpost.html', title='viewpost', post=post)

    if user_id:
        user_id = int(user_id)
        user = User.query.get(user_id)
        user_posts = user.blogs
        return render_template('viewuser.html', title='viewuser', user=user, user_posts=user_posts)

    posts = Blog.query.order_by(Blog.created.desc()).all()

    return render_template('posts.html', title='posts', posts=posts)


@app.route('/')
def index():

    contributors = User.query.all()
    contributors = User.query.order_by(User.username.asc()).all()

    return render_template('index.html', title='contributors', contributors=contributors)


@app.route('/login', methods=['POST', 'GET'])
def login():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        # no errors
        if user and check_pw_hash(password, user.pw_hash):
            session['username'] = username
            return redirect('/newpost')

        # errors
        elif not user:
            flash('Username not found', 'error_username')

        # errors
        else:
            flash('Username Password combo not found', 'error_password')

        # provide state of attempted form
        return render_template('login.html',
            title='login',
            username=username,
            password=password)

    return render_template('login.html',
        title='login')


@app.route('/logout', methods=['POST'])
def logout():
    del session['username']
    return redirect('/blog')


@app.before_request
def require_login():
    allowed_routes = ['static', 'signup', 'login', 'blog', 'index']
    if request.endpoint not in allowed_routes and 'username' not in session:
        return redirect('/login')


app.secret_key = '^N#W-q<t,F2zmQ#'

if __name__ == '__main__':
    app.run()
