from django.db import models


class Booking(models.Model):
    class Meta:
        managed = False
        db_table = 'Booking'

    id = models.IntegerField(primary_key=True)
    listing_id = models.IntegerField()
    customer_id = models.IntegerField()
    check_in = models.TextField()
    check_out = models.TextField()
    price = models.FloatField()
    number_of_guests = models.IntegerField()

    def __str__(self):
        return str(self.id) + ' ' + str(self.listing_id) + ' ' + str(self.customer_id) + ' ' + str(self.check_in) + ' ' \
               + str(self.check_out) + ' ' + str(self.price) + ' ' + str(self.number_of_guests)

