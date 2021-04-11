from django.db import models


class NewListing(models.Model):
    class Meta:
        managed = False

    name = models.TextField()
    description = models.TextField()
    house_rules = models.TextField()
    accommodates = models.IntegerField()
    cancellation_policy = models.TextField()
    room_type = models.TextField()
    property_type = models.TextField()
    amenities = models.TextField()
    picture_url = models.URLField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    city = models.TextField()
    street = models.TextField()
    state = models.TextField()
    zip_code = models.TextField()
    score = models.IntegerField()
    start_date = models.TextField()
    end_date = models.TextField()
    price = models.IntegerField()
