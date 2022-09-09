from django.urls import path

from follower import views

app_name = "follower"

urlpatterns = [
    path("add/<int:pk>/", views.AddFollower.as_view(), name="follower-add"),
    path("remove/<int:pk>/", views.RemoveFollower.as_view(), name="follower-delete")
]
