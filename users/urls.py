from django.contrib import admin
from django.urls import path, include
from .views import ContactView, Chackout, TestimonialView, UserRegisterView, UserLoginView, LogOutView, MyProfileView

urlpatterns = [
    path('chackout/', Chackout.as_view(), name='chackout'),
    path('testimonial/', TestimonialView.as_view(), name='testimonial'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('profile/', MyProfileView.as_view(), name='profile')

]

