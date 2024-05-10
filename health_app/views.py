from django.views.generic import TemplateView
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login
from patients.forms import RegisterForm, UpdateProfileForm
from django.contrib.auth.decorators import login_required
from patients.models import Patient
# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

@login_required
def profile(request):
    return render(request, 'profile.html')


@login_required
def update_user(request):
    current_user = User.objects.get(id=request.user.id)
    profile_user = Patient.objects.get(user__id=request.user.id)
    user_form = RegisterForm(request.POST or None, request.FILES or None, instance=current_user)
    profile_form = UpdateProfileForm(request.POST or None, request.FILES or None, instance=profile_user)
    if user_form.is_valid() and profile_form.is_valid():
        user_form.save()
        profile_form.save()
        login(request, current_user)
        return redirect('home')
    return render(request, 'update_user.html', {'user_form':user_form, 'profile_form':profile_form})
