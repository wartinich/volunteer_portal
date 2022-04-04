from django.urls import path
from comments.api.views import CreateCommentView


urlpatterns = [
    path('create/', CreateCommentView.as_view(), name='create_comment'),
]
