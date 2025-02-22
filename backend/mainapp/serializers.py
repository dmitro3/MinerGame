from rest_framework import serializers
from .models import *

class TelegramUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramUser
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'lvl', 'comp_lvl', 'webcam_lvl', 'micro_lvl', 'user']

    # Если вам нужно включить сериализацию связанных объектов, 
    # вы можете использовать вложенные сериализаторы или PrimaryKeyRelatedField
    user = serializers.PrimaryKeyRelatedField(queryset=TelegramUser.objects.all())


class Payments_costSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments_cost
        fields = '__all__'
