from django.urls import path
from .views import SearchListView

app_name = 'searchapp'

urlpatterns = [

    path('', SearchListView.as_view(), name='searchResult'),

]
