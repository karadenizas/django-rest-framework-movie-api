from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from django.urls import path, include

from .views import (
    ReviewViewSet,
    MovieViewSet,
    CommentViewSet,
)

router = DefaultRouter()
router.register(r'reviews', ReviewViewSet, basename='reviews')
router.register(r'movies', MovieViewSet, basename='movies')
router.register(r'comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('', include(router.urls)),
    # if the search will have the number of pages, I manually set the url
    path(
        'movies/search/<str:search>/<str:page>/',
        MovieViewSet.as_view(actions={'get': 'movie_search'}),
        name='movie-search-page'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


