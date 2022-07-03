from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('aid/', include('apps.assistances.urls')),
    path('user/', include('apps.users.urls')),
    path('comment/', include('apps.comments.urls')),
]