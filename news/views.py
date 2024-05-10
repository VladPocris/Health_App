from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import News
from django.urls import reverse_lazy

# Create your views here.
class NewsListView(ListView):
    paginate_by = 12
    model = News
    template_name = 'news/news.html'
    context_object_name = "all_news_list"

class NewsDetailView(DetailView):
    model = News
    template_name = 'news/news_detail.html'

class NewsCreateView(CreateView):
    model = News
    template_name = 'news/news_new.html'
    fields = ['title', 'link', 'image']

class NewsUpdateView(UpdateView):
    model = News
    template_name = 'news/news_edit.html'
    fields = ['title', 'image']

class NewsDeleteView(DeleteView):
    model = News
    template_name = 'news/news_delete.html'
    success_url = reverse_lazy('news_list')