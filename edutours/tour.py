from datetime import datetime
from .city import City

class Tour:
    def __init__(self, name, description, image, price, language, city, date):
        self.name = name
        self.description = description
        self.image = image
        self.price = price
        self.language = language
        self.city = city
        self.date = date
    
    def get_tour_details(self):
        return str(self)

    def __repr__(self):
        return f"Name: {self.name}, Description: {self.description}, Image: {self.image}, Price: {self.price}, City: {self.city}, Date: {self.date}\n" 