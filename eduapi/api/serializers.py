from rest_framework import serializers

from .models import Node


class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = ('id', 'slug', 'depth', 'path')
        read_only_fields = ('depth', 'path')
