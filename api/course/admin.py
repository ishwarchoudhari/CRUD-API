from django.contrib import admin
from .models import Course, EnrolledUsers

# Register your models here.


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "author", "price")

@admin.register(EnrolledUsers)
class EnrolledUserAdmin(admin.ModelAdmin):
    list_display =('id','user','course','joined_date')

