from celery import shared_task
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from user_profile.services.utils import generate_token


@shared_task(bind=True)
def send_verify_email(user, request):
    current_site = get_current_site(request)
    email_subject = "Activate your account"
    email_body = render_to_string("email/verified_email.html", {
        "user": user,
        "domain": current_site,
        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
        "token": generate_token.make_token(user)
    })
    send_mail(subject=email_subject, message=email_body, recipient_list=[user.email])
