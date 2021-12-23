from rest_framework import serializers

from movies.models import Movie, Review, Comment


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = ['review', 'user', 'content', 'review_rating', 'create_time']


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Review
        fields = ['movie', 'user', 'content', 'movie_rating', 'create_time']


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = [
            'imdb_id', 'title', 'year',
            'runtime', 'genre', 'director',
            'writer', 'actor', 'plot',
            'language', 'poster', 'type',
            'create_time'
        ]
        read_only_fields = [
            'imdb_id', 'title', 'year',
            'runtime', 'genre', 'director',
            'writer', 'actor', 'plot',
            'language', 'poster', 'type',
            'create_time'
        ]