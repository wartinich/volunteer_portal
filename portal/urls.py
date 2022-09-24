from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

from portal import settings

schema_view = get_swagger_view(title='Volunteer portal API')

urlpatterns = [
    path('admin/', admin.site.urls),

    path("auth/", include("authentication.urls")),
    path("auth/", include("social_django.urls"), name="social"),
    path("profile/", include("user_profile.urls")),
    path("follower/", include("follower.urls")),
    path("user/", include("user.urls")),
    path("assitance/", include("assistance.urls")),
    path("petition/", include("petition.urls")),

    path("api/", include("api.urls")),
    path("swagger/", schema_view),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
