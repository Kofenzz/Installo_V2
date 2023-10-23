import json
from django.core.management.base import BaseCommand
from adress.models import City

class Command(BaseCommand):
    help = 'Populate city data from a JSON file'

    def handle(self, *args, **kwargs):
        with open('static/data/cities.json', 'r') as json_file:
            data = json.load(json_file)
            for item in data:
                city_name = item['city']
                county_name = item['county']
                City.objects.get_or_create(name=city_name, county=county_name)