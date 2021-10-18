from django.db.models import fields
from rest_framework import serializers
from .models import *


class ParentUserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParentUser
        fields = '__all__'
    


class ChildUserModelSerializer(serializers.ModelSerializer):

    parent = ParentUserModelSerializer(read_only=True)
    class Meta:
        model = ChildUser
        fields = '__all__'
        depth = 1
        
