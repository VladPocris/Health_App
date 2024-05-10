from django.urls import path, include
from .views import NewsDeleteView, NewsListView, NewsDetailView, NewsCreateView, NewsUpdateView

urlpatterns = [
    path('', NewsListView.as_view(), name ='news_list'),
    path('search/', include('searchapp.urls')),
    path('<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
    path('new/', NewsCreateView.as_view(), name='news_new'),
    path('<int:pk>/edit/', NewsUpdateView.as_view(), name='news_edit'),
    path('<int:pk>/delete/', NewsDeleteView.as_view(), name='news_delete'),
]