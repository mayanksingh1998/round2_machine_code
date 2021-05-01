from ride_sharing.models import Ride
import constants
import logging

log = logging.getLogger('ride_sharing')


class RideHelper(object):

    @classmethod
    def add_ride(cls, **kwargs):

        pick_up_location = kwargs.get(constants.RIDES.PICK_UP_LOCATION)
        drop_location = kwargs.get(constants.RIDES.DROP_LOCATION)
        price = kwargs.get('price')
        ride_dict = {constants.RIDES.PICK_UP_LOCATION: pick_up_location,
                     constants.RIDES.DROP_LOCATION: drop_location,
                     'price': price }
        print(ride_dict)

        try:
            ride = Ride.objects.create(**ride_dict)
            return ride.to_json()
        except Exception as e:
            log.error(str(e))
            raise Exception(" Unable to create a ride at this moment")
        return False

    @classmethod
    def is_ride_exist(cls, ride_id):
        try:
            ride = Ride.objects.get(id=ride_id).exists()
            return True
        except Ride.DoesNotExist:
            raise Exception("ride does not exist")

        return False

    @classmethod
    def get_rides(cls, **kwargs):
        filters = {}
        pickup_location = kwargs.get(constants.RIDES.PICK_UP_LOCATION)
        drop_location = kwargs.get(constants.RIDES.DROP_LOCATION)
        created_on = kwargs.get(constants.RIDES.CREATED_ON)

        if pickup_location:
            filters.update({constants.RIDES.PICK_UP_LOCATION: pickup_location})


        if drop_location:
            filters.update({constants.RIDES.DROP_LOCATION: drop_location})


        if created_on:
            filters.update({constants.RIDES.CREATED_ON: created_on})

        try:
            rides = Ride.objects.filter(**filters)
        except:
            raise Exception("unable to get")
