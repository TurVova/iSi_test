from django.urls import path

from dialogs.views import ThreadCreateCreateAPIView

urlpatterns = [
    path('create/thread/', ThreadCreateCreateAPIView.as_view()),
    # path('update/', views.CustomUserRetrieveUpdateAPIView.as_view()),
    # path('auth/', views.authenticate_user),
]
