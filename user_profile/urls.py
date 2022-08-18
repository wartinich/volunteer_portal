from django.urls import path

from user_profile import views

app_name = "user_profile"

urlpatterns = [
    path("", views.ProfileView.as_view(), name="profile"),
    path("update/", views.ProfileUpdateView.as_view(), name="profile-update"),
    path(
        "password_change/",
        views.CustomPasswordChangeView.as_view(),
        name="password-change"
    )
]
