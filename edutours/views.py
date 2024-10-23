# Flask routes handling requests
from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/city')
def city():
    return render_template('city.html')

@bp.route('/tour')
def tour():
    return render_template('tour.html')

@bp.route('/order')
def order():
    return render_template('order.html')

