from flask import Blueprint
from flask import render_template, url_for, flash, redirect, request
from gratitudeapp.users.forms import RegistrationForm, LoginForm, UpdateAccountForm, RequestResetForm, ResetPasswordForm
from gratitudeapp.models import User, Post
from gratitudeapp import bcrypt, db
from flask_login import login_user, current_user, logout_user
from gratitudeapp.users.utils import save_picture, send_reset_email

errors = Blueprint('errors', __name__)

@errors.app_errorhandler(404)
def error_404(error):
    return render_template('errors/404.html'), 404 #render template doesn't use url_for

@errors.app_errorhandler(403)
def error_403(error):
    return render_template('errors/403.html'), 403

@errors.app_errorhandler(500)
def error_500(error):
    return render_template('errors/500.html'), 500
