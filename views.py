import urllib, json
import logging

from datetime import datetime
from django.http import HttpResponse
from django.db import transaction

from .models import Event
from .validation_lookups import VALID_PAYLOAD_URLS, VALID_CATEGORIES


logger = logging.getLogger('logger_name')

def update_eye_data(request, payload_site_slug):
    """Applications will request this view with its slug to off load their payload the The Eye's database.
    I am assuming that the application calls to this view is scheduled in order to allow time for the The Eye to update.
    """

    if not request.user.is_authenticated: # Assume there's a way to authenticate the requestor
        return HttpResponse(status=500)

    try:
        response = urllib.request.urlopen(VALID_PAYLOAD_URLS[payload_site_slug]) 
        data = json.loads(response.read())  # Assuming the data is a JSON list of Events
        error_list = [] # Gathers a list of dicts of the errors found

        with transaction.atomic():
            events = []
            for event in data:
                errors = check_event_error(event)
                if errors:
                    error_list.append(errors)
                events.append(Event(session_id=event['session_id'], category=event['category'], name=event['name'], data=event['data'], timestamp=event['timestamp'], has_errors=len(error_list) > 0))
            Event.objects.bulk_create(events)
            logger.warning('Event errors found: %s' % error_list)

        return HttpResponse("Updated")
    except Exception as ex:
        logger.error(ex)


async def get_event_info(request):
    pass



def check_event_error(event):
    """Check if the event has errors a returns a dict as a report"""

    errors = {}
    category = event.get('category', None)
    name = event.get('name', None)
    timestamp = event.get('timestamp', None)

    now = datetime.now()

    if not name:
        errors['name'] = 'None'
    if not timestamp:
        errors['timestamp'] = 'None'

    if not category:
        errors['category'] = 'None'
    elif not VALID_CATEGORIES.get(category, None):
        errors['category'] = 'No such category'
    elif name and name not in VALID_CATEGORIES[category]['valid_names']:
        errors['name'] = 'Invalid name in category'
    
    if timestamp and datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S.%f') > datetime.now():
        errors['timestamp'] = 'Invalid time'

    if errors:
        errors['event'] = event
    
    return errors