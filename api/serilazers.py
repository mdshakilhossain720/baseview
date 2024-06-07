from rest_framework import serializers
from .models import Student


class StudentSerilazer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['id','name','roll','city']

   
