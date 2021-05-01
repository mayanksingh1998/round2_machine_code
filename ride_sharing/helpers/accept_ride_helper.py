from ride_sharing.models import Ride
import constants
import logging
from ride_sharing.models import RideDriver
log = logging.getLogger('ride_sharing')


class AcceptRideHelper(object):

    @classmethod
    def accept_ride(cls, ride_id, driver_id):
        if ride_id and driver_id:
            ride_driver = {'ride_id': ride_id,
                         'driver_id': driver_id}
        try:
            ride_driver = RideDriver.objects.create(**ride_driver)
            return ride_driver
        except Exception as e:
            log.error(str(e))
            raise Exception(" Unable to accept the ride at this moment")
        return False
