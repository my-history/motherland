from rest_framework import serializers
from ..base.models import BaseUser


class BaseUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BaseUser
        fields = ['']
