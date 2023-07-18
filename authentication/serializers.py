from .models import User
from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField



class UserCreationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=25,)
    email = serializers.EmailField(max_length=80, )
    phone_number = PhoneNumberField(null=False, allow_blank =False)
    password= serializers.CharField(min_lenght= 8)



    class Meta:
        model= User
        fields = ['username','email','phone_number','password']


    def validate(self, attrs):
        return super().validate(attrs)