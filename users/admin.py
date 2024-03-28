from django.contrib import admin
from .models import UserProfile, Comments, Problems
from import_export.admin import ImportExportModelAdmin


@admin.register(UserProfile)
class UserProfileAdmin(ImportExportModelAdmin):
    list_display = ['user', 'age']
    search_fields = ['age']
    list_display_links = ['age']
    ordering = ['age']

@admin.register(Comments)
class CommentsAdmin(ImportExportModelAdmin):
    list_display = ['comment_title', 'comment']
    search_fields = ['comment_title']
    list_display_links = ['comment_title']
    ordering = ['comment_title']


@admin.register(Problems)
class ProblemAdmin(ImportExportModelAdmin):
    list_display = ['problem_name', 'problem_description']
    search_fields = ['problem_name']
    list_display_links = ['problem_name']
    ordering = ['problem_name']

