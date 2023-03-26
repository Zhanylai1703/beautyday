from rest_framework import serializers

from apps.otzyv.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = (
            'id',
            'name',
            'description',
            'quality',
            'atmosphere',
        )