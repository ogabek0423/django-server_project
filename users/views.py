from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth.mixins import LoginRequiredMixin


class Chackout(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'users/chackout.html')


class ContactView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'users/contact.html')


class TestimonialView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'users/testimonial.html')


class UserLoginView(View):
    def get(self, request):
        form = UserLoginForm()
        context = {'form': form}
        return render(request, 'users/login.html', context)

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        data = {
            "username": username,
            "password": password
        }
        login_form = AuthenticationForm(data=request.POST)

        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)

            return redirect("index")
        else:

            context = {
                "form": login_form,
            }
            return render(request, "users/login.html", context)


class UserRegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        context = {'form': form}
        return render(request, 'users/register.html', context)


    def post(self, request):
        create_form = UserRegisterForm(data=request.POST)
        if create_form.is_valid():
            create_form.save()
            return redirect('login')

        else:
            context = {'form': create_form}
            return render(request, 'users/register.html', context)


class LogOutView(View):
    def get(self, request):
        logout(request)

        return redirect('index')



