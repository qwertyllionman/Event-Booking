from django.urls import path

from apps.views import CreateEventAPIView, CreateRegisterAPIView, ListRegistrationsAPIView, ListEventsAPIView

urlpatterns = [
    path('api/v1/event/create', CreateEventAPIView.as_view()),
    path('api/v1/event/list', ListEventsAPIView.as_view()),
    path('api/v1/registration/create', CreateRegisterAPIView.as_view()),
    path('api/v1/registration/list', ListRegistrationsAPIView.as_view()),
]