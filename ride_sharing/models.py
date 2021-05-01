from django.db import models
import constants

from constants.driver import STATUS, DRIVER

class Driver(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, default=None, db_index=True)
    phone = models.CharField(max_length=25, db_index=True, blank=True, null=True, default=None)
    status = models.CharField(max_length=10, choices=(
        ('active', 'Active'),
        ('inactive', 'Inactive')), default='active', db_index=True)

    def to_json(self):
        return{
            'name': self.name,
            'phone': self.phone,
            'status': self.status
        }


class Ride(models.Model):
    pickup_location = models.CharField(max_length=255, blank=True, null=True, default=None, db_index=True)
    drop_location = models.CharField(max_length=255, blank=True, null=True, default=None, db_index=True)
    price = models.IntegerField(max_length=255, blank=True, null=True, default=None, db_index=True)
    status = models.CharField(max_length=10, choices=(
        ('active', 'Active'),
        ('inactive', 'Inactive')), default='active', db_index=True)

    created_on = models.DateTimeField(db_index=True, auto_now_add=True)

    def to_json(self):
        return {
            'pickup_location': self.pickup_location,
            'drop_location': self.drop_location,
            'price': self.price,
            'status': self.status
        }

class RideDriver(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    rider = models.ForeignKey(Ride, on_delete=models.CASCADE)
