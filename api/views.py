from django.shortcuts import render

from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from api.serializers import CoursSerializer
from api.models import Cours

# Create your views here.
class ListCoursAPIView(ListAPIView):
    """This endpoint list all of the available cours from the database"""
    queryset = Cours.objects.all()
    serializer_class = CoursSerializer

class CreateCoursAPIView(CreateAPIView):
    """This endpoint allows for creation of a cours"""
    queryset = Cours.objects.all()
    serializer_class = CoursSerializer

class UpdateCoursAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific cours by passing in the id of the cours to update"""
    queryset = Cours.objects.all()
    serializer_class = CoursSerializer

class DeleteCoursAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Cours from the database"""
    queryset = Cours.objects.all()
    serializer_class = CoursSerializer