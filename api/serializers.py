from django.db.models import fields
from rest_framework import serializers
from .models import *


class ParentUserModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = ParentUserModel
        fields = '__all__'


class ChildUserModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ChildUserModel
        fields = ['child_first_name', 'child_last_name', 'parent']




class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = '__all__'
        

class BookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book
        fields = '__all__'
        