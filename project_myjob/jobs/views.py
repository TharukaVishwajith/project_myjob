from django.shortcuts import render
from .models import Job
from rest_framework import viewsets
from .serializers import JobSerializer

# Create your views here.
class JobView(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer