from django.urls import path
from .views import RegisterAPIView, LoginAPIView, UserProfileDataView, BookmarkAPIView
urlpatterns=[
    path('register/',RegisterAPIView.as_view(),name='register'),
    path('login/',LoginAPIView.as_view(),name='login'),
    path('user_profile/<str:username>/', UserProfileDataView.as_view(), name='user-profile'),
    path('bookmark/', BookmarkAPIView.as_view(), name='bookmark_api'),
]