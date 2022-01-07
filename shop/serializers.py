from rest_framework import serializers
from shop.models import Review

# DRF(djangorestframework) 를 이용할 때는 form 이 아니라 serializer 사용


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"