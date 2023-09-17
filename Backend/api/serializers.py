from rest_framework import serializers
from .models import CustomUser#Contact
# from .models import Tag

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'        
        # fields = ('id', 'name', 'email', 'password', 'role_type', 'mobile', 'address','specilist','degree')
        extra_kwargs = {'password': {'write_only': True}}


        
# class ContactSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Contact
#         fields = '__all__'        