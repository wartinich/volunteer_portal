from django.urls import path

from petition import views

app_name = "petition"

urlpatterns = [
    path("", views.PetitionListView.as_view(), name="petition-list"),
    path("detail/<int:pk>/", views.PetitionDetailView.as_view(), name="petition-detail")
]
