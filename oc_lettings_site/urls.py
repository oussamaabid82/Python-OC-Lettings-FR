from django.contrib import admin
from django.urls import include, path

from oc_lettings_site import views


urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include('letting.urls')),
    path('profiles/', include('profiles.urls')),
    path('admin/', admin.site.urls),
]
