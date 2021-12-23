from django.contrib import admin

from movies.models import Movie, Review, Comment 

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('imdb_id', 'title',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('review', 'user',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('movie', 'user', 'movie_rating',)
