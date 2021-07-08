from django.http import JsonResponse

# Create your views here.


def home(requests):
    return JsonResponse({'info': 'Django'})
