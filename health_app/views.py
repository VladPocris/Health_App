from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

@login_required
def profile(request):
    return render(request, 'profile.html')