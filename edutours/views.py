# Flask routes handling requests
from flask import Blueprint, render_template
from .models import City, Tour, Order
from datetime import datetime

# data
# Cities in Taiwan
taipei = City('1', 'Taipei', 'Capital city of Taiwan, famous for its street food and night markets.', 'taipei.jpg')
taichung = City('2', 'Taichung', 'Famous for its vibrant street food scene and beautiful parks.', 'taichung.jpg')
kaohsiung = City('3', 'Kaohsiung', 'Port city with delicious seafood and local markets.', 'kaohsiung.jpg')

# Cooking Educational Tours
tour1 = Tour('1', 'Beef Noodle Soup', 'Join us for a hands-on cooking class where you will learn to make authentic Taiwanese Beef Noodle Soup, including tips on making the perfect broth and tender beef.', 'beef_noodle.jpg', 60.00, taipei, ['MON', 'WED'], "14:00 - 16:00", ["English, Mandarin"], True)
tour2 = Tour('2', 'Xiao Long Bao', 'Learn to craft delicious Xiao Long Bao in this interactive cooking class, mastering the art of making the perfect dumpling wrappers and flavorful soup filling.', 'xiao_long_bao.jpg', 65.00, taipei, ['MON', 'WED'], "14:00 - 16:00", ["English, Mandarin"], True)
tour3 = Tour('3', 'Sun Cake', 'Discover the secrets behind making traditional Taichung Sun Cakes, a flaky pastry filled with maltose and sweet flavors, in this fun baking class.', 'sun_cake.jpg', 50.00, taichung, ['MON', 'WED'], "14:00 - 16:00", ["English, Mandarin"], True)
tour4 = Tour('4', 'Taichung Street Food Experience', 'Join our street food cooking class to learn how to make popular Taichung snacks like Popcorn Chicken and Grilled Corn, bringing the night market experience to your kitchen.', 'taichung_street_food.jpg', 45.00, taichung, ['MON', 'WED'], "14:00 - 16:00", ["English, Mandarin"], True)
tour5 = Tour('5', 'Kaohsiung Seafood Cooking Class', 'Dive into the world of fresh seafood with our expert chef as you learn to prepare classic Kaohsiung seafood dishes using local ingredients.', 'kaohsiung_seafood.jpg', 70.00, kaohsiung, ['MON', 'WED'], "14:00 - 16:00", ["English, Mandarin"], True)
tour6 = Tour('6', 'Kaohsiung Fruit Dessert Workshop', 'Learn to create stunning desserts using seasonal fruits from Kaohsiung in this hands-on workshop that celebrates local flavors.', 'kaohsiung_fruit_dessert.jpg', 55.00, kaohsiung, ['MON', 'WED'], "14:00 - 16:00", ["English, Mandarin"], False)

# List of cities and tours
cities = [taipei, taichung, kaohsiung]
tours = [tour1, tour2, tour3, tour4, tour5, tour6]

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html', cities=cities)

@bp.route('/city/<int:city_id>/')
def city(city_id):
    city_tours = []
    for tour in tours:
        if int(tour.city.id) == int(city_id): 
            city_tours.append(tour)  

    city_info = None
    for city in cities:
        if int(city.id) == int(city_id): 
            city_info = city
            print("city", city)

    return render_template('city.html', cities=cities, city=city_info, tours=city_tours)

@bp.route('/tour/<int:tour_id>/')
def tour(tour_id):
    tour_info = None
    for tour in tours:
        if int(tour.id) == int(tour_id):
            tour_info = tour
    return render_template('tour.html', cities=cities, tour=tour_info)

@bp.route('/order')
def order():
    return render_template('order.html', cities=cities)

