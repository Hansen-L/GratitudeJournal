from flask import render_template, url_for, flash, redirect, request, abort
from gratitudeapp.posts.forms import PostForm
from gratitudeapp.models import Post
from gratitudeapp import db
from flask_login import current_user, login_required
from datetime import datetime


from flask import Blueprint

posts = Blueprint('posts', __name__)

@posts.route("/post/new", methods=['GET','POST'])
@login_required
def new_post():
    form = PostForm()
    if Post.query.filter_by(date_posted=datetime.utcnow().date()):
        flash('You have already made an entry for today! You can edit your entry by clicking on the corresponding date', 'info')
        return redirect(url_for('main.home'))
    if form.validate_on_submit():
        post1 = Post(title=form.title1.data, content=form.content1.data, author=current_user)
        db.session.add(post1)
        db.session.commit()
        if form.title2.data: #if there is a second entry
            post2 = Post(title=form.title2.data, content=form.content2.data, author=current_user)
            db.session.add(post2)
            db.session.commit()
        if form.title2.data:
            post3 = Post(title=form.title3.data, content=form.content3.data, author=current_user)
            db.session.add(post3)
            db.session.commit()
        flash('Your gratitude has been saved!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='New Entry', form=form, legend='New Entry')

@posts.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)

@posts.route("/date/<int:y>/<int:m>/<int:d>/update", methods=['GET','POST'])
@login_required
def update_post(y, m, d):
    posts = Post.query.filter_by(date_posted=datetime(y, m, d)).all()
    if posts[0].author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        posts[0].title = form.title1.data
        posts[0].content = form.content1.data
        posts[1].title = form.title2.data
        posts[1].content = form.content2.data
        posts[2].title = form.title3.data
        posts[2].content = form.content3.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('main.home'))
    elif request.method == 'GET':
        form.title1.data = posts[0].title
        form.content1.data = posts[0].content
        form.title2.data = posts[1].title
        form.content2.data = posts[1].content
        form.title3.data = posts[2].title
        form.content3.data = posts[2].content
    return render_template('create_post.html', title='Update Post', form=form, legend='Update Post')

# @posts.route("/post/<int:post_id>/update", methods=['GET','POST'])
# @login_required
# def update_post(post_id):
#     post = Post.query.get_or_404(post_id)
#     if post.author != current_user:
#         abort(403)
#     form = PostForm()
#     if form.validate_on_submit():
#         post.title = form.title.data
#         post.content = form.content.data
#         db.session.commit()
#         flash('Your post has been updated!', 'success')
#         return redirect(url_for('posts.post', post_id=post.id))
#     elif request.method == 'GET':
#         form.title.data = post.title
#         form.content.data = post.content
#     return render_template('create_post.html', title='Update Post', form=form, legend='Update Post')

@posts.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.home'))





