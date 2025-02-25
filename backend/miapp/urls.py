from django.urls import path
from .views import search_movies
from django.http import JsonResponse

def health_check(request):
    return JsonResponse({"status": "ok"})

urlpatterns = [
    path('api/search/', search_movies, name='search_movies'),
    path('health/', health_check),
]
