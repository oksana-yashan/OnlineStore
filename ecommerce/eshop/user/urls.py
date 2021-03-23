from django.urls import include, path
from . import views


urlpatterns = [
    path('all/', views.UserList.as_view(), name='full_list'),
    path('current/', views.CurrentUserProfile.as_view(), name='current'),
    path('current/update/', views.CurrentUserProfile.as_view(), name='current_update'),
    path('register/', views.RegisterUser.as_view(), name='register'),

]