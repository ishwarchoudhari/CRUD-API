from rest_framework import serializers
from api.course.models import Course
from api.user.model import CustomUser
from .models import UserWishlist


class UserSerializer( serializers.ModelSerializer ) :
    class Meta :
        model = CustomUser
        fields = '_all_'


class CourseSerializer( serializers.ModelSerializer ) :
    class Meta :
        model = Course
        fields = ('name' , 'author' , 'price' , 'date')


class WishlistSerializer(serializer.ModelSerializer ) :
    user = UserSerializer( many = True , read_only = True )
    course = CourseSerializer( many = True , read_only = True )

    class Meta :
        model = UserWishlist
        fields = ('user' , 'course')