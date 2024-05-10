from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, UpdateProfileForm, UpdateUserForm
from .models import Patient

class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'registration/signup.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='home')

        return render(request, self.template_name, {'form': form})


@login_required
def profile(request):
     if request.method == 'POST':
          user_form = UpdateUserForm(request.POST, instance=request.user)
          profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

          if user_form.is_valid() and profile_form.is_valid():
               user_form.save()
               profile_form.save()
               messages.success(request, 'Your Profile has been updated!')
               return redirect(to='users-profile')
     else:
          user_form = UpdateProfileForm(instance=request.user)
          profile_form = UpdateProfileForm(instance=request.user.profile)

     return render(request, 'profile.html', {'user_form': user_form, 'profile_form': profile_form})    

def patient_list(request):
     patients = Patient.objects.all()
     return render(request, 'profile.html', {'patients': patients})
