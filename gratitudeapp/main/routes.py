from flask import render_template, request, Blueprint, flash
from gratitudeapp.models import Post
from more_itertools import consecutive_groups

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    per_page=9
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=per_page)

    dates = Post.query.order_by(Post.date_posted.desc()).with_entities(Post.date_posted).distinct().all()
    ordinal_dates = []
    for d in dates:
        ordinal_dates.append(-d[0].toordinal())
    x = [list(group) for group in consecutive_groups(ordinal_dates)]
    streak = -x[0][0] + x[0][-1] + 1
    if streak > 1:
        flash(f'You are on a {streak} day gratitude streak! Keep it up :)','success')

    return render_template('home.html',posts=posts, per_page=per_page, streak=streak)

@main.route("/about")
def about():
    return render_template('about.html', title='about')


# Post.query.order_by(Post.date_posted.desc()).with_entities(Post.date_posted).distinct().all()