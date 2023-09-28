from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.views import View
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

class SignupView(FormView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('profile')  # Replace 'profile' with the URL name for the user's profile page

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = reverse_lazy('profile')  # Replace 'profile' with the URL name for the user's profile page

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)
