from django.urls import path

from profiles import views as views_profile

app_name = 'profiles'

urlpatterns = [
    path('', views_profile.profiles_index, name='profiles_index'),
    path('<str:username>/', views_profile.profile, name='profile'),
]
