from django.urls import path

from user import views

app_name = "user"

urlpatterns = [
    path("", views.UserListView.as_view(), name="user-list"),
    path("detail/<int:pk>/", views.UserDetailView.as_view(), name="user-detail")
]
