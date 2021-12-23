from django.db import models

from users.models import MyUser


class Movie(models.Model):
    imdb_id = models.CharField(max_length=12, primary_key=True)
    title = models.CharField(max_length=255)
    year = models.CharField(max_length=55)
    runtime = models.CharField(max_length=55)
    genre = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    writer = models.CharField(max_length=255)
    actor = models.CharField(max_length=255)
    plot = models.TextField(max_length=2500)
    language = models.CharField(max_length=255)
    poster = models.URLField()
    type = models.CharField(max_length=255)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.imdb_id}'


class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),        
    )
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    user = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    content = models.TextField(max_length=10000)
    movie_rating = models.PositiveIntegerField(choices=RATING_CHOICES)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.movie_rating} by {self.user}'


class Comment(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),        
    )
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    user = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    content = models.TextField(max_length=2500, null=True, blank=True)
    review_rating = models.PositiveIntegerField(choices=RATING_CHOICES)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.content[:10]} by {self.user}'