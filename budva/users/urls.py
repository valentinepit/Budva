from django.urls import path
from . import views as users

app_name = 'users'

urlpatterns = [
    path('', users.UsersListView.as_view(), name='users_list'),
    path('create/', users.UsersCreateView.as_view(), name='users_create'),
    path('login/', users.login, name='login'),
    path('logout/', users.logout, name='logout'),
    path('user/<int:pk>/', users.UserDetailView.as_view(), name='users_detail'),
    path('update/<int:pk>/', users.UserUpdateView.as_view(), name='users_edit'),
    path('delete/<int:pk>/', users.UserDeleteView.as_view(), name='users_delete'),
]