from django.urls import path

from accounts import views
from accounts.views import (
    CreateCustomUserAPIView,
    CustomUserRetrieveUpdateAPIView,
    UserLoginAPIView
)
app_name = 'accounts'
urlpatterns = [
    path('create/', CreateCustomUserAPIView.as_view(), name='create'),
    path('update/', CustomUserRetrieveUpdateAPIView.as_view()),
    path('login/', UserLoginAPIView.as_view(), name='login'),
    path('auth/', views.authenticate_user),
]
