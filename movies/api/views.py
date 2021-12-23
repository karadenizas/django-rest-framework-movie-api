from django.http.response import HttpResponse
import requests

from rest_framework import status, viewsets
from rest_framework.decorators import action, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from django.conf import settings
from rest_framework.views import APIView

from movies.models import Comment, Movie, Review
from .pagination import MyStandartPagination
from .serializers import CommentSerializer, MovieSerializer, ReviewSerializer
from .permissions import IsOwnerOrReadOnly


class MovieViewSet(viewsets.ViewSet):

    def get_object(self, pk):
        try:
            movie = Movie.objects.get(imdb_id=pk)
            return movie

        except Movie.DoesNotExist:
            payload = {"apikey": settings.API_KEY, "i": pk}
            get_url = requests.get('http://www.omdbapi.com', params=payload)
            get_json = get_url.json()
            movie = Movie.objects.create(
                imdb_id=pk,
                title=get_json['Title'],
                year=get_json['Year'],
                runtime=get_json['Runtime'],
                genre=get_json['Genre'],
                director=get_json['Director'],
                writer=get_json['Writer'],
                actor=get_json['Actors'],
                plot=get_json['Plot'],
                language=get_json['Language'],
                poster=get_json['Poster'],
                type=get_json['Type'],
            )
            return movie

    @action(
        methods=['get'], detail=False, url_path='search/(?P<search>[^/.]+)'
    )
    def movie_search(self, request, search, page=None):
        payload = {"apikey": settings.API_KEY, "s": search, "page": page}
        get_url = requests.get('http://www.omdbapi.com', params=payload)
        return Response(get_url.json())

    def list(self, request):
        queryset = Movie.objects.all()
        type = request.query_params.get('type', None)
        if type is not None:
            queryset = queryset.filter(type=type)
        paginator = MyStandartPagination()
        page = paginator.paginate_queryset(queryset, request)
        if page is not None:
            serializer = MovieSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            serializer = MovieSerializer(queryset, many=True)
            return Response(serializer.data)
    
    @action(methods=['get'], detail=True, url_path='reviews')
    def movie_reviews(self, request, pk):
        queryset = Review.objects.filter(movie_id=pk)
        paginator = MyStandartPagination()
        page = paginator.paginate_queryset(queryset, request)
        if page is not None:
            serializer = ReviewSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            serializer = ReviewSerializer(queryset, many=True)
            return Response(serializer.data)

    def retrieve(self, request, pk):
        queryset = self.get_object(pk=pk)
        serializer = MovieSerializer(queryset)
        return Response(serializer.data)


class ReviewViewSet(viewsets.ViewSet):
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]

    def list(self, request):
        queryset = Review.objects.all()
        paginator = MyStandartPagination()
        page = paginator.paginate_queryset(queryset, request)
        if page is not None:
            serializer = ReviewSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            serializer = ReviewSerializer(queryset, many=True)
            return Response(serializer.data)

    @action(methods=['get'], detail=True, url_path='comments')
    def review_comments(self, request, pk):
        queryset = Comment.objects.filter(review_id=pk)
        paginator = MyStandartPagination()
        page = paginator.paginate_queryset(queryset, request)
        if page is not None:
            serializer = CommentSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            serializer = CommentSerializer(queryset, many=True)
            return Response(serializer.data)

    def create(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
    
    def retrieve(self, request, pk=None):
        queryset = Review.objects.get(pk=pk)
        serializer = ReviewSerializer(queryset)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        queryset = Review.objects.get(pk=pk)
        serializer = ReviewSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

    def partial_update(self, request, pk=None):
        queryset = Review.objects.get(pk=pk)
        serializer = ReviewSerializer(
            queryset, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                serializer.error, status=status.HTTP_400_BAD_REQUEST
            )
    
    def destroy(self, request, pk=None):
        queryset = Review.objects.get(pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentViewSet(viewsets.ViewSet):
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]

    def list(self, request):
        queryset = Comment.objects.all()
        paginator = MyStandartPagination()
        page = paginator.paginate_queryset(queryset, request)
        if page is not None:
            serializer = CommentSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            serializer = CommentSerializer(queryset, many=True)
            return Response(serializer.data)

    def create(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
    
    def retrieve(self, request, pk=None):
        queryset = Comment.objects.get(pk=pk)
        serializer = CommentSerializer(queryset)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = Comment.objects.get(pk=pk)
        serializer = CommentSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

    def partial_update(self, request, pk=None):
        queryset = Comment.objects.get(pk=pk)
        serializer = CommentSerializer(
            queryset, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                serializer.error, status=status.HTTP_400_BAD_REQUEST
            )
    
    def destroy(self, request, pk=None):
        queryset = Comment.objects.get(pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)