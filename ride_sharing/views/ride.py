from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from ride_sharing.helpers.ride_helper import RideHelper
import constants
from rest_framework.exceptions import ValidationError, APIException, PermissionDenied
import logging
from django.http import JsonResponse

log = logging.getLogger('ride_sharing')
import json
class Ride(APIView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.replay_json_response = True
        self.ride_helper = RideHelper()

    authentication_classes = [authentication.TokenAuthentication]

    def validate_and_get_post_request_params(self, request):
        query_params = json.loads(request.body)
        pickup_location = query_params.get(constants.RIDES.PICK_UP_LOCATION, None)
        drop_location = query_params.get(constants.RIDES.DROP_LOCATION, None)
        price = query_params.get('price')

        if not pickup_location:
            raise ValidationError("unable to get the pickup location")

        if not drop_location:
            raise ValidationError("please provide your drop location")

        return {
            constants.RIDES.PICK_UP_LOCATION: pickup_location,
            constants.RIDES.DROP_LOCATION: drop_location,
            "price": price
        }

    def post(self, request):
        try:
            req_params = self.validate_and_get_post_request_params(request)
            ride = self.ride_helper.add_ride(**req_params)
        except Exception as e:
            log.exception('Exception while creating ride - %s' % e)
            raise APIException("unable to add")

        else:
            return JsonResponse({constants.RIDES.RIDE_ID: ride, 'message': 'Ride created successfully'})

