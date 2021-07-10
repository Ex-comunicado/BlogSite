from os import name
from flask import redirect, url_for
import flask_login
from blogmain import db
from flask.helpers import flash
from blogmain.form import BlogPostForm, LoginForm, NameForm, RegisterForm
from blogmain import app
from flask import render_template
from blogmain.models import BlogPosts, Users
from flask_login import login_user, logout_user, login_required, current_user

@app.route("/")
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/aboutme', methods=['GET','POST'])
def about_me():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash("Form submitted successfully!", category='success')
    return render_template('aboutme.html', 
        name = name,
        form = form
    )

@app.route('/writeblog', methods=['GET','POST'])
@login_required
def write_blog():
    form = BlogPostForm()
    if form.validate_on_submit():
        post = BlogPosts(title=form.title.data,
                        content = form.content.data,
                        author = form.author.data,
                        slug = form.slug.data
        )
        db.session.add(post)
        db.session.commit()
        form.title.data = ''
        form.author.data = ''
        form.content.data = ''
        form.slug.data = ''
        flash('Blog post created successfully!', category="success")
    return render_template('writeblog.html', form=form)

@app.route('/posts/<int:id>')
def post(id):
    post = BlogPosts.query.get_or_404(id)
    return render_template('post.html', post=post)

@app.route('/posts/edit/<int:id>', methods=['GET','POST'])
def edit_posts(id):
    post = BlogPosts.query.get_or_404(id)
    form = BlogPostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.author = form.author.data
        post.slug = form.slug.data
        post.content = form.content.data
        db.session.add(post)
        db.session.commit()
        flash('Post updated successfully', category="success")
        return redirect(url_for('post', id=post.id))
    form.title.data = post.title
    form.author.data = post.author
    form.slug.data = post.slug
    form.content.data = post.content
    return render_template('edit_post.html', form=form)


@app.route('/viewblogs')
@login_required
def view_blogs():
    viewblogs = BlogPosts.query.order_by(BlogPosts.date_posted)
    is_non_empty = bool(viewblogs)
    return render_template('viewblogs.html', viewblogs=viewblogs)

@app.route('/register', methods=['GET','POST'])
def register_user():
    form = RegisterForm()
    if form.validate_on_submit():
        user = Users(username=form.username.data,
                    email=form.email_addr.data,
                    password=form.password1.data
                    )
        db.session.add(user)
        db.session.commit()
        form.username.data = ''
        form.email_addr.data = ''
        form.password1.data = ''
        form.password2.data = ''
        login_user(user)
        flash(f'Accounted Created Successfully! You are now logged in as {user.username}', category="success")
        return redirect(url_for('home_page'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'Kindly review this error: {err_msg}', category='danger')
    return render_template('register.html',form = form)

@app.route('/login', methods=['GET','POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = Users.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password(attempted_password=form.password.data):
            login_user(attempted_user)
            flash(f'Success! You are logged in as {attempted_user.username}', category="success")
            return redirect(url_for('home_page'))
        else:
            flash('Username or password is incorrect.', category="danger")

    return render_template('login.html', form = form)

@app.route('/logout')
def logout_page():
    logout_user()
    flash('You have been logged out.', category="info")
    return redirect(url_for('home_page'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500