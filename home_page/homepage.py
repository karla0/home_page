from flask import ( Blueprint, render_template )

bp = Blueprint('homepage', __name__)

@bp.route('/')
def index():
    return render_template('homepage/index.html')

@bp.route('/contact')
def contact():
    return render_template('homepage/contact.html')

@bp.route('/resume')
def resume():
    return render_template('homepage/resume.html')

@bp.route('/portfolio')
def portfolio():
    return render_template('homepage/portfolio.html')