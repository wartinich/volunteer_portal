from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("auth/", include("authentication.urls")),
    path("profile/", include("user_profile.urls")),
    path("assitance/", include("assistance.urls"))
]
