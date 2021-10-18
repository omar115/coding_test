from rest_framework import serializers
from .models import *


# Parent Model Serializer
class ParentUserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParentUser
        fields = '__all__'
    
    
# child Model Serializer
class ChildUserModelSerializer(serializers.ModelSerializer):

    street = serializers.SerializerMethodField('get_street', read_only=True, required=False)
    city = serializers.SerializerMethodField('get_city', read_only=True, required=False)
    state = serializers.SerializerMethodField('get_state', read_only=True, required=False)
    zip = serializers.SerializerMethodField('get_zip', read_only=True, required=False)

    def get_street(self, obj):
        if obj.parent_user:
            return obj.parent_user.street
        return ""

    def get_city(self, obj):
        if obj.parent_user:
            return obj.parent_user.city
        return ""
    
    def get_state(self, obj):
        if obj.parent_user:
            return obj.parent_user.state
        return ""
    
    def get_zip(self, obj):
        if obj.parent_user:
            return obj.parent_user.zip_code
        return ""
    class Meta:
        model = ChildUser
        fields = '__all__'
        validators = []
        
