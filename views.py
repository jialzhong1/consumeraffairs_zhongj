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

    # if not request.user.is_authenticated: # Assume there's a way to authenticate the requestor
    #     return HttpResponse(status=500)

# {
#   "session_id": "e2085be5-9137-4e4e-80b5-f1ffddc25423",
#   "category": "form interaction",
#   "name": "submit",
#   "data": {
#     "host": "www.consumeraffairs.com",
#     "path": "/",
#     "form": {
#       "first_name": "John",
#       "last_name": "Doe"
#     }
#   },
#   "timestamp": "2021-01-01 09:15:27.243860"
# }

    try:
        response = urllib.request.urlopen(VALID_PAYLOAD_URLS[payload_site_slug]) 
        data = json.loads(response.read())  # Assuming the data is a JSON list of Events

        with transaction.atomic():
            pass

        return HttpResponse("Updated")
    except Exception as ex:
        pass
        # logger.error(ex)


async def get_event_info(request):
    pass