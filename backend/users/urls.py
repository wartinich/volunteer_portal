from django.urls import path
from users.api.views import UserListView, UserDetailView, UserUpdateView

urlpatterns = [
    path('all/', UserListView.as_view(), name='users_list'),
    path('detail/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='user_update')

]
