from rest_framework.serializers import ModelSerializer

from apps.models import User, Event, Registration


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class RegisterSerializer(ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'