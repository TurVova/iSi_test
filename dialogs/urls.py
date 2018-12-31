from django.urls import path

from dialogs.views import (
    ThreadCreateAPIView,
    MessageCreateAPIView,
    UserThreadsListAPIView,
    MessageThreadRetrieveAPIView,
    ThreadRetrieveUpdateAPIView
)

app_name = 'dialogs'
urlpatterns = [
    path('create/thread/', ThreadCreateAPIView.as_view(), name='create-thread'),
    path('list/user-threads/', UserThreadsListAPIView.as_view(), name='list-thread'),
    path('create/message/', MessageCreateAPIView.as_view(), name='create-message'),
    path(
        'list/messages-thread/<int:pk>/', MessageThreadRetrieveAPIView.as_view(),
         name='list-messages-tread'
    ),
    path(
        'delete-update/thread/<int:pk>/', ThreadRetrieveUpdateAPIView.as_view(),
        name='delete-update-thread'),
]
