from django.conf.urls import include, url

urlpatterns = [
    url(r'^ride_sharing/', include('ride_sharing.urls')),
]


