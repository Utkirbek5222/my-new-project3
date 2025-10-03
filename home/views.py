from django.http import HttpResponse
from rest_framework import viewsets
from .models import Course
from .serializers import CourseSerializer
from django.shortcuts import render
def hindex(request):
    return HttpResponse("testing home page")
# Create your views here.
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filterset_fields = {
        'title':['exact', 'icontains'],
        'slug':['exact']
    }
    search_fields = ['title', 'keywords']
