from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError, APIException, PermissionDenied
from ride_sharing.helpers.ride_helper import RideHelper
import constants
import logging
from django.http import JsonResponse
import json

log = logging.getLogger('ride_sharing')

class RideHistory(APIView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.replay_json_response = True
        self.rides_helper = RideHelper()

    authentication_classes = [authentication.TokenAuthentication]

    def validate_and_request_params(self, request):
        query_params = json.loads(request.body)
        pickup_location = query_params.get(constants.RIDES.PICK_UP_LOCATION, None)
        drop_location = query_params.get(constants.RIDES.DROP_LOCATION, None)
        created_on = query_params.get(constants.RIDES.CREATED_ON, None)

        return {
            constants.RIDES.PICK_UP_LOCATION: pickup_location,
            constants.RIDES.DROP_LOCATION: drop_location,
            constants.RIDES.CREATED_ON: created_on
        }

    def get(self, request):
        req_params = self.validate_and_request_params(request)
        print(req_params)
        try:
            rides = self.rides_helper.get_rides(**req_params)
        except Exception as e:
            log.exception('Exception while adding driver - %s' % e)
            raise APIException("unable to add")

        else:
            return JsonResponse({'rides': rides, 'message': 'success'})


