from django.http import HttpResponse

from . import views
from .models import *

def index(request):
    return HttpResponse("hello")