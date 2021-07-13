from django.contrib import admin
from .models import UserWishlist
# Register your models here.

@admin.register(UserWishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display=('id','user','course')

