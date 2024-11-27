from django.urls import path

from .views import output_services, output_service, create_record

from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('services/', output_services),
    path('service/<int:pk>', output_service),
    path('create_record/', csrf_exempt(create_record)),
]
