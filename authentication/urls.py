from django.urls import path

from authentication import views

app_name = "authentication"

urlpatterns = [
    path("sign_up/", views.RegisterView.as_view(), name="sign_up"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("password_reset/", views.ResetPasswordView.as_view(), name="password-reset"),
    path(
        "password_reset/done/",
        views.ResetPasswordDoneView.as_view(),
        name="password-reset-done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        views.ResetPasswordConfirmView.as_view(),
        name="password-reset-confirm",
    ),
    path(
        "reset/done/",
        views.ChangePasswordCompleteView.as_view(),
        name="password-reset-complete",
    )
]
