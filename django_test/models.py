from django.db import models
from django_test.settings import KEY_API_GOOGLE, URL_API_GOOGLE
import requests


class User(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    status_geo = models.BooleanField(default=False)

    objects = models.Manager()

    def __str__(self):
        return self.first_name

    def as_json(self):
        payload = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'address': self.address,
            'city': self.city,
        }
        return payload

    def get_location(self):
        latitude = None
        longitude = None
        url = "{}address={}&key={}".format_map(URL_API_GOOGLE, self.address, KEY_API_GOOGLE)
        response = requests.get(url)

        if response.status_code == '200':
            data = response.content
            if data['status'] == 'OK':
                latitude = data['results'][0]['geometry']['location']['lat']
                longitude = data['results'][0]['geometry']['location']['lng']

        if latitude and longitude:
            self.latitude = latitude
            self.longitude = longitude
            self.status_geo = True
            self.save()

        return self




