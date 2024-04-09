from celery_docker.celery import app
from send_email.models import Contact
from django.core.mail import send_mail


@app.task
def send_spam(user_email):
    send_mail(
        "one time",
        "one time",
        "test@gmail.com",
        [user_email],
        fail_silently=False,
    )


@app.task
def send_spam_beats():
    contacts = Contact.objects.all()
    for contact in contacts:
        send_mail(
            contact.name,
            "every minute",
            "sdfbhabd@gmail.com",
            [contact.email],
            fail_silently=False,
        )
