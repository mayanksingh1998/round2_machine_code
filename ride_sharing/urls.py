from django.urls import path
from ride_sharing import views
from ride_sharing.views import Driver

app_name = 'ride_sharing'

urlpatterns = [
    path('drivers/new/', Driver.as_view()),
    path('ride/<int:ride_id>/', views.AcceptRide.as_view()),
    path('ride/new/', views.Ride.as_view()),
    path('rides/', views.RideHistory.as_view()),

]
