from django.urls import path
from assistances.api.views import CreateAidView, ListAidView, UpdateAidView, DetailAidView


urlpatterns = [
    path('create/', CreateAidView.as_view(), name='create_aid'),
    path('all/', ListAidView.as_view(), name='list_aid'),
    path('detail/<int:id>/', DetailAidView.as_view(), name='detail_aid'),
    path('update/<int:id>/', UpdateAidView.as_view(), name='update_aid')
]
