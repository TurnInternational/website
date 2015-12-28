from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('website.urls', namespace='home')),
    url(r'^admin/', admin.site.urls),
]