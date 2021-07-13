from rest_framework import serializers
from .models import Course, EnrolledUsers

class EnrolledUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = EnrolledUsers
		fields = ('user','joined_date')

class CourseSerializer(serializers.ModelSerializer):
	enrolled_user = EnrolledUserSerializer(many=True,read_only=True)
	class Meta:
		model = Course
		fields = ('name', 'author', 'price', 'date','enrolled_user')