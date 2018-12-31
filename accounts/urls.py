from django.urls import path

from accounts.views import (
    CreateCustomUserAPIView,
    UserLoginAPIView
)

app_name = 'accounts'
urlpatterns = [
    path('register/', CreateCustomUserAPIView.as_view(), name='create'),
    path('login/', UserLoginAPIView.as_view(), name='login'),
]
