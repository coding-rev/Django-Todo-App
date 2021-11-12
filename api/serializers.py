from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
	class Meta:
		model 	= Todo 
		fields 	= ["id", "body", "done"]

class EditSerializer(serializers.Serializer):
	body 		= serializers.CharField()
	done 		= serializers.BooleanField()
