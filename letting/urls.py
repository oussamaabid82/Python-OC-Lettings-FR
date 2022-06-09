from django.urls import path

from . views import lettings_index, letting

app_name = 'letting'

urlpatterns = [
    path('', lettings_index, name='lettings_index'),
    path('<int:letting_id>/', letting, name='letting'),
]
