from django.shortcuts import render
from rest_framework import viewsets
from restUygulama.models import Yazar,Kitap
from restUygulama.serializers import YazarSerializer,KitapSerializer

# Create your views here.

class YazarViewSet(viewsets.ModelViewSet):

    queryset = Yazar.objects.all()
    serializer_class = YazarSerializer

class KitapViewSet(viewsets.ModelViewSet):
   
   
    queryset = Kitap.objects.all()
    serializer_class = KitapSerializer