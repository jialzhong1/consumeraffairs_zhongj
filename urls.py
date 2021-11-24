from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('update_eye_data/<slug:payload_site_slug>/', views.update_eye_data, name='update_eye_data'),
    path('get_event_info/(?P<session_id>\w+)/(?P<category>\w+)/(?P<start_time>\w+)/(?P<end_time>\w+)/', views.get_event_info, name='get_event_info'),
]
