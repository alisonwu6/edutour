# Flask routes handling requests
from flask import Blueprint, render_template
from .models import City, Tour, Order
from datetime import datetime

# data
# Cities in Taiwan
taipei = City('1', 'Taipei', 'Capital city of Taiwan, famous for its street food and night markets.', 'taipei.jpg')
tainan = City('2', 'Tainan', 'Known for its traditional Taiwanese snacks and historic sites.', 'tainan.jpg')
kaohsiung = City('3', 'Kaohsiung', 'Port city with delicious seafood and local markets.', 'kaohsiung.jpg')

# Cooking Educational Tours
# tour1 = Tour('1', 'Taipei Cooking Class: Beef Noodles', 'Join us for a hands-on cooking class in Taipei where you will learn to make traditional Taiwanese Beef Noodles. Discover the rich flavors and techniques behind one of Taiwan’s most iconic dishes.', 'beef_noodles.jpg', 50.00, taipei, datetime(2023, 11, 25))
# tour2 = Tour('2', 'Taipei Cooking Class: Xiao Long Bao', 'Learn to make Xiao Long Bao, the famous Taiwanese soup dumplings, in this hands-on cooking class in Taipei. Perfect for food lovers looking to master this delicate and delicious dish.', 'xiao_long_bao.jpg', 55.00, taipei, datetime(2023, 11, 26))

tour1 = Tour('1', 'Taipei Night Market Tour', 'Learn to cook Taiwanese street food like stinky tofu and scallion pancakes.', 'night_market.jpg', 60.00, taipei, datetime(2023,11,15))
tour2 = Tour('2', 'Tainan Traditional Snacks Workshop', 'Cook Tainan specialties like milkfish congee and coffin bread.', 'tainan_snacks.jpg', 75.00, tainan, datetime(2023,12,5))
tour3 = Tour('3', 'Kaohsiung Seafood Masterclass', 'Catch and cook fresh seafood dishes, including milkfish and squid.', 'kaohsiung_seafood.jpg', 100.00, kaohsiung, datetime(2023,12,20))

# List of cities and tours
cities = [taipei, tainan, kaohsiung]
tours = [tour1, tour2, tour3]

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html', cities=cities)

@bp.route('/city')
def city():
    return render_template('city.html', )

@bp.route('/tours')
def tours():
    return render_template('tours.html')

@bp.route('/order')

def order():
    return render_template('order.html')

