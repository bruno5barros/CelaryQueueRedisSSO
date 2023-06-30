from django.urls import path
from customers.views import send_email


urlpatterns = [
    path("say_hello/", send_email)
]
