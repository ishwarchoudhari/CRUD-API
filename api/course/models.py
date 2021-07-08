from django.db import models
from api.category.models import Category
from api.user.models import User
# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    date = models.DateField()
    is_active = models.BooleanField(default=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    users = models.ManyToManyField(User)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
