from rest_framework import serializers
from .models import PublicRelations

class PublicRelationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicRelations
        fields = ('id','title','author','content','display')