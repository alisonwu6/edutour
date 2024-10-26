# Flask routes handling requests
from flask import Blueprint, render_template
from .models import City, Tour, Order
from . import db

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    cities = db.session.scalars(db.select(City).order_by(City.id)).all()
    return render_template('index.html', cities=cities)

@main_bp.route('/city/<int:city_id>/')
def city(city_id):
    cities = db.session.scalars(db.select(City).order_by(City.id)).all()
    tours = db.session.scalars(db.select(Tour).where(Tour.city_id == city_id)).all()
    selected_city = db.session.get(City, city_id)
    print("selected_city", selected_city)
    return render_template('city.html', cities=cities, tours=tours, city=selected_city)

@main_bp.route('/tour/<int:tour_id>/')
def tour(tour_id):
    cities = db.session.scalars(db.select(City).order_by(City.id)).all()
    tour_info = db.session.get(Tour, tour_id)
    return render_template('tour.html', cities=cities, tour=tour_info)

# Stubs
@main_bp.route('/order', methods=['POST','GET'])
def order():
    return 'not implemented yet'

@main_bp.route('/deleteorder')
def deleteorder():
    return 'not implemented yet'

@main_bp.route('/deleteorderitem', methods=['POST'])
def deleteorderitem():
    return 'not implemented yet'

@main_bp.route('/checkout', methods=['POST','GET'])
def checkout():
    return 'not implemented yet'
