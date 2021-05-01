from rest_framework.views import APIView

from rest_framework.exceptions import ValidationError, APIException, PermissionDenied
from ride_sharing.helpers.accept_ride_helper import AcceptRideHelper
import constants
import logging
from django.http import JsonResponse
import json
log = logging.getLogger('ride_sharing')

class AcceptRide(APIView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.replay_json_response = True
        self.accept_ride_helper = AcceptRideHelper()


    def validate_ride(self, ride_id):
        return self.rider_helper.is_ride_exist(ride_id=ride_id)


    def post(self, request, ride_id):
        validate_ride = self.validate_ride(ride_id)
        query_params = json.loads(request.body)

        driver_id = query_params.get(constants.DRIVER.DRIVER_ID)
        if validate_ride:
            try:
                driver = self.accept_ride_helper.accept_ride(ride_id)
            except Exception as e:
                log.exception('Exception while adding driver - %s' % e)
                raise APIException("unable to add")

            else:
                return {constants.DRIVER.DRIVER_ID: driver, 'message': 'accepted ride  successfully'}


