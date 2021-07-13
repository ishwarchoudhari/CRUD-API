from django.db import models
from api.category.models import Category
from api.user.models import CustomUser

class Course(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    date = models.DateField()
    is_active = models.BooleanField(default=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class EnrolledUsers(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='enrolled')
    course = models.ForeignKey(Course,on_delete=models.PROTECT,related_name='enrolled_users')
    joined_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user}-{self.course}'