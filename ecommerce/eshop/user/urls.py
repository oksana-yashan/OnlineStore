from django.urls import include, path
from . import views


urlpatterns = [
    path('all/', views.UserList.as_view(), name='full_list'),
    path('current/', views.CurrentUserProfile.as_view(), name='current'),
    path('current/update/', views.CurrentUserProfile.as_view(), name='current_update'),
    path('register/', views.RegisterUser.as_view(), name='register'),

    path('delete/<str:user_id>/', views.deleteUser, name='user_delete'),
    path('update/<str:user_id>/', views.updateUser, name='user_update'),
    path('<str:user_id>/', views.getUserById, name='user'),
    

]