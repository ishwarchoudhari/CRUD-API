from django.urls import path, include
from .views import home
from rest_framework.authtoken import views



urlpatterns = [
    path('', home, name='api.home'),
    path("category/", include('api.category.urls')),
    path('course/', include('api.course.urls')),
    path('user/', include('api.user.urls')),
    path('api-token-auth/', views.obtain_auth_token, name='api_token_auth'),
]
