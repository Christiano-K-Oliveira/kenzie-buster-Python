from rest_framework import serializers
from movies.models import RatingsChoices, Movie
from users.serializers import RegistroSerializer
import ipdb


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    synopsis = serializers.CharField(allow_null=True, default=None)
    rating = serializers.ChoiceField(
        choices=RatingsChoices.choices,
        default=RatingsChoices.G
    )
    duration = serializers.CharField(allow_null=True, required=False)
    added_by = serializers.SerializerMethodField(read_only=True)

    def create(self, validated_data: dict) -> Movie:
        return Movie.objects.create(**validated_data)
    
    def get_added_by(self, obj):
        return obj.user.email
