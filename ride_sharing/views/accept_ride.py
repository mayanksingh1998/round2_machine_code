from rest_framework.views import APIView

from rest_framework.exceptions import ValidationError, APIException, PermissionDenied
from ride_sharing.helpers.accept_ride_helper import AcceptRideHelper
import constants
import logging
from django.http import JsonResponse
from ride_sharing.helpers.ride_helper import RideHelper
import json
log = logging.getLogger('ride_sharing')

class AcceptRide(APIView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.replay_json_response = True
        self.accept_ride_helper = AcceptRideHelper()
        self.ride_helper = RideHelper()


    def validate_ride(self, ride_id):
        return RideHelper.is_ride_exist(ride_id=ride_id)


    def post(self, request, ride_id):
        validate_ride = self.validate_ride(ride_id)
        query_params = json.loads(request.body)

        driver_id = query_params.get(constants.DRIVER.DRIVER_ID)
        if validate_ride:
            try:
                driver = self.accept_ride_helper.accept_ride(ride_id, driver_id)
            except Exception as e:
                log.exception('Exception while adding driver - %s' % e)
                raise APIException("unable to add")

            else:
                return JsonResponse({'message': 'accepted ride  successfully'})


