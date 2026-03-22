from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import get_user_model
from allauth.account.adapter import get_adapter


@shared_task
def test_task():
    print("Celery works!")
    

@shared_task
def send_email_task(subject, message, to_email):

    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [to_email],
        fail_silently=False,
    )
    

User = get_user_model()


@shared_task
def send_allauth_email_task(context, template_prefix, to_email):

    User = get_user_model()
    # Pull the user back out of the DB using the ID we sent
    context['user'] = User.objects.get(pk=context['user_id'])
    
    # Now that 'user' is an object again, render_mail will work
    adapter = get_adapter()
    adapter.render_mail(template_prefix, to_email, context).send()
