from django.urls import path
from .views import all_events, add_event, update_event, remove_event, calendar_app

urlpatterns = [
    path('', calendar_app, name='calendar_app'),
    path('all_events/', all_events, name='all_events'), 
    path('add_event/', add_event, name='add_event'), 
    path('update_event/', update_event, name='update_event'),
    path('remove_event/', remove_event, name='remove_event'),
]