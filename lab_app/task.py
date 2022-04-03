from ast import arg
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def sent_mail_user(email,name):
    subject="Nano Innovation Labs"
    message=f'Hi,{name}\nyour experiment details successfully got in our end'
    send_mail(subject,message,settings.EMAIL_HOST_USER,[email],fail_silently=False)
    return "success"