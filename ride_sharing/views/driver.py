from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError, APIException, PermissionDenied
from ride_sharing.helpers.driver_helper import DriverHelper
import constants
import logging
import json
from django.http import JsonResponse
log = logging.getLogger('ride_sharing')


class Driver(APIView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.replay_json_response = True
        self.driver_helper = DriverHelper()

    def validate_and_get_post_request_params(self, request):
        body = json.loads(request.body)
        print(body)
        name = body.get(constants.DRIVER.NAME, constants.DRIVER.DEFAULT_NAME)
        phone = body.get(constants.DRIVER.PHONE, constants.DRIVER.DEFAULT__PHONE)
        print(not name)
        if not name:
            raise ValidationError("Please provide the name")

        if not phone:
            raise ValidationError("Please provide the phone")

        return {
            constants.DRIVER.NAME: name,
            constants.DRIVER.PHONE: phone
        }

    def post(self, request):
        req_params = self.validate_and_get_post_request_params(request)
        try:
            driver = self.driver_helper.add_driver(**req_params)
            print(driver)
        except Exception as e:
            print(e)
            log.exception('Exception while adding driver - %s' % e)
            raise APIException("unable to add")

        else:
            return JsonResponse({constants.DRIVER.DRIVER: driver, 'message': 'driver added successfully'})
