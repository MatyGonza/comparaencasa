from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TitleBasics
from .serializers import TitleBasicsSerializer

@api_view(['GET'])
def search_movies(request):
    query = request.GET.get('q', '')
    if query:
        movies = TitleBasics.objects.filter(primaryTitle__icontains=query)
    else:
        movies = TitleBasics.objects.all()
    serializer = TitleBasicsSerializer(movies, many=True)
    return Response(serializer.data)