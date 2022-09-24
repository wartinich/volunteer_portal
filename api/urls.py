from django.urls import path

from api.views import AssistanceViewSet

app_name = "api"

urlpatterns = [
    path("assistance/", AssistanceViewSet.as_view({"get": "list"})),
    path("assistance/detail/<int:pk>/", AssistanceViewSet.as_view({"get": "retrieve"}))
]
