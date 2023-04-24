from rest_framework import serializers
from movies.models import RatingsChoices, Movie, MovieOrder
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



class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.SerializerMethodField(read_only=True)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    buyed_by = serializers.SerializerMethodField(read_only=True)
    buyed_at = serializers.DateTimeField(read_only=True)

    def create(seld, validated_data: dict) -> Movie:
        return MovieOrder.objects.create(**validated_data)

    def get_buyed_by(self, obj):
        return obj.user.email
    
    def get_title(self, obj):
        return obj.movie.title
