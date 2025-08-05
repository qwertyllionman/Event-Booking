from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Model, CharField, TextChoices, DateField, DateTimeField, ForeignKey, CASCADE


class User(AbstractUser):
    first_name = None
    last_name = None
    username = CharField(max_length=255, unique=True)
    email = CharField(max_length=255, unique=True)
    password = CharField(max_length=255)

class Event(Model):
    title = CharField(max_length=255)
    description = CharField(max_length=255)
    date = DateField()
    location = CharField(max_length=255)
    organizer_id = ForeignKey("apps.User", CASCADE, related_name='events')

class Registration(Model):
    user = ForeignKey('apps.User', CASCADE, related_name='registrations')
    event = ForeignKey('apps.Event', CASCADE, related_name='registrations')
    registered_at = DateTimeField(auto_now_add=True)