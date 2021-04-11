from django.db import models


class Search(models.Model):
    class Meta:
        managed = False

    destination = models.TextField()
    from_date = models.TextField()
    to_date = models.TextField()
    num_guests = models.IntegerField()

