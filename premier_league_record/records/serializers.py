from rest_framework import serializers
from .models import Match, AugustFixture

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'

class AugustFixtureSerializer(serializers.ModelSerializer):
    class Meta:
        model = AugustFixture
        fields = '__all__'
