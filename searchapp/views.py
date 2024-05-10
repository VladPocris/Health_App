from django.shortcuts import render
from news.models import News
from django.views.generic import ListView
from django.db.models import Q
# Create your views here.

class SearchListView(ListView):
    paginate_by = 12
    model = News
    context_object_name = 'all_news_list'
    template_name = 'searchapp/searchapp.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return News.objects.filter(Q(title__icontains=query))

    def get_context_data(self, **kwargs):
        context = super(SearchListView, self).get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context