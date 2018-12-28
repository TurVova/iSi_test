from django.urls import path, include

from accounts import views

urlpatterns = [
    path('create/', views.CreateCustomUserAPIView.as_view()),
    path('update/', views.CustomUserRetrieveUpdateAPIView.as_view()),
    path('auth/', views.authenticate_user),
]
