from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from .forms import UserLoginForm, UserRegisterForm, UserProblemForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Problems, Comments, UserProfile


class Chackout(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'users/chackout.html')


class ContactView(LoginRequiredMixin, View):
    def get(self, request):
        form = UserProblemForm()
        context = {'form': form}
        return render(request, 'users/contact.html', context)

    def post(self, request):
        first_name = request.POST['first_name']
        email = request.POST['email']
        problem = request.POST['problem']
        problem_t = request.POST['problem_title']

        a = Problems.objects.create(problem_name=problem_t, problem_description=problem,
                                    firstname=first_name, email=email)
        a.save()
        return redirect('thank')


class TestimonialView(LoginRequiredMixin, View):
    def get(self, request):
        # user = User.objects.filter(username__icontains=request.USER)
        context = {'testimonial': Comments.objects.all(),
                   # 'user': user
        }

        return render(request, 'users/testimonial.html', context)


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


class MyProfileView(View):
    def get(self, request):
        user = User.objects.get(username=request.user.username)
        # try:
        #     userprofile = UserProfile.objects.get(user_id=user.id)
        # except userprofile.DoesNotExist:
        #     context = {'user': user}
        #     return render(request, 'users/my_profile.html', context)
        # else:

        context = {
                'user': user,
            }
        return render(request, 'users/my_profile.html', context)



