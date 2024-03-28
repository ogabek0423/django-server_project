from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User


from products.models import Product, Bestsellers, FeaturedItems


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    image = models.ImageField(upload_to='media/users/u_pics')
    age = models.IntegerField()

    def __str__(self):
        return f'{self.user.first_name}'


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_title = models.CharField(max_length=200)
    comment = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.comment_title}'


class Problems(models.Model):
    firstname = models.CharField(max_length=30)
    email = models.EmailField()
    problem_name = models.CharField(max_length=30)
    problem_description = models.TextField()

    def __str__(self):
        return f'{self.problem_name}'

