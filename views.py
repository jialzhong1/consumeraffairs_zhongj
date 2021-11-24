import urllib, json
import logging

from django.http import HttpResponse
from django.db import transaction

from .models import Event
from .valid_payload_urls import VALID_PAYLOAD_URLS


logger = logging.getLogger('logger_name')

def update_eye_data(request, payload_site_slug):
    """Applications will request this view with its slug to off load their payload the The Eye's database.
    I am assuming that the application calls to this view is scheduled in order to allow time for the The Eye to update.
    """

    try:
        response = urllib.request.urlopen(VALID_PAYLOAD_URLS[payload_site_slug]) 
        data = json.loads(response.read())  # Assuming the data is a JSON list of Events

        with transaction.atomic():
            pass

        return HttpResponse("Updated")
    except Exception as ex:
        logger.error(ex)


async def get_event_info(request):
    pass