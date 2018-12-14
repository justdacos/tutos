from rest_framework import serializers
from . import models

class utilisateursSerializer(serializers.ModelSerializer)
  
  class Meta:
  	model = models.utilisateurs
    fields = '__all__'
   