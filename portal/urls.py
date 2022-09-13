from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from portal import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("auth/", include("authentication.urls")),
    path("profile/", include("user_profile.urls")),
    path("follower/", include("follower.urls")),
    path("user/", include("user.urls")),
    path("assitance/", include("assistance.urls")),
    path("petition/", include("petition.urls"))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
