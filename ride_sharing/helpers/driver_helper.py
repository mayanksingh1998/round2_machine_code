from ride_sharing.models import Driver
import constants
import logging
log = logging.getLogger('ride_sharing')

class DriverHelper(object):

    @classmethod
    def add_driver(cls, **kwargs):

        name = kwargs.get(constants.DRIVER.NAME)
        phone = kwargs.get(constants.DRIVER.PHONE)
        driver_dict = {constants.DRIVER.NAME: name,
                       constants.DRIVER.PHONE: phone}
        try:
            driver = Driver.objects.create(**driver_dict)
            return driver.to_json()
        except Exception as e:
            print(e)
            log.error(str(e))
            raise Exception(" Unable to add Driver at this moment")
