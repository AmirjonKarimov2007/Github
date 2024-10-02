from django.urls import path
from .views import profilesview,profileview,login_user,logout_user,register_user
app_name = 'users'
urlpatterns = [
    path('',profilesview,name='profiles'),
    path('profile/<uuid:id>/',profileview,name='profile'),
    path('register/',register_user,name='register'),
    path('login/',login_user,name='login'),
    path('logout/',logout_user,name='logout')
    ]