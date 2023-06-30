from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .tasks import notify_customers


@api_view(["GET", "POST"])
def send_email(request):
    notify_customers.delay("Hello")

    return Response("Email sent", status=status.HTTP_200_OK)
