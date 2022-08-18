from django.urls import path

from assistance import views

app_name = "assistance"

urlpatterns = [
    path("", views.AssistanceListView.as_view(), name="assistance-list"),
    path("create/", views.AssistanceCreateView.as_view(), name="assistance-create"),
    path("detail/<int:pk>/", views.AssistanceDetailView.as_view(), name="assistance-detail"),
    path("delete/<int:pk>/", views.AssistanceDeleteView.as_view(), name="assistance-delete")
]
