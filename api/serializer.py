from rest_framework import serializers
from .models import book

class bookSerializer(serializers.ModelSerializer):
    class Meta:
        model=book
        fields=["id", "title", "author", "price"]