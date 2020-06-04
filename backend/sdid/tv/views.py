from django.shortcuts import render
from rest_framework import generics
from .models import PublicRelations
from .serializers import PublicRelationsSerializer


class PublicRelationsListCreate(generics.ListCreateAPIView):
    queryset = PublicRelations.objects.all()
    serializer_class = PublicRelationsSerializer
