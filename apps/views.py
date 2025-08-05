from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework.generics import CreateAPIView, ListAPIView

from apps.models import Event, Registration
from apps.serializers import EventSerializer, RegisterSerializer

@extend_schema(tags=['Event API'], responses=EventSerializer)
class CreateEventAPIView(CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

@extend_schema(tags=['Register API'], responses=RegisterSerializer)
class CreateRegisterAPIView(CreateAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegisterSerializer

@extend_schema(tags=['Event API'])
class ListEventsAPIView(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

@extend_schema(tags=['Register API'])
class ListRegistrationsAPIView(ListAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegisterSerializer


