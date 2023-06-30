from time import sleep
from celery import shared_task


@shared_task
def notify_customers(message):
    print("Send 10k emails..")
    print(message)
    sleep(20)
    print("Done Now!!!!!!!!!")