from rest_framework import serializers

from apps.team.models import Team, Gallary


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = (
            'id',
            'name', 
            'last_name',
            'photo',
        )


class GallarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallary
        fields = (
            'photo',
        )