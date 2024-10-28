from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import UserAccount
from mini_twitter.utils import send_custom_email

from .tasks import send_email_birthdate


@receiver(post_save, sender=UserAccount)
def user_account_create_handler(sender, instance: UserAccount, created, **kwargs):
    created = True
    if created:
        message = f'Hello, welcome {instance.username} to mini twitter project!'
        subject = 'Create account'
        to_user = instance.email
        print("aniver", instance.date_of_birth)
        send_custom_email(subject, message, [to_user])
        # chamar task para envio de email de feliz aniversario
        scheduled_date = instance.date_of_birth
        send_email_birthdate.apply_async((instance.username,), eta=scheduled_date)

@receiver(post_save, sender=UserAccount)
def user_follow_handler(sender, instance: UserAccount, created, **kwargs):
    if not kwargs['update_fields']:
        return
    #if 'total_followers' in kwargs['update_fields']:
    message = f'Hello, you have a new follower!'
    subject = 'New follower'
    to_user = instance.email
    send_custom_email(subject, message, [to_user])

post_save.connect(user_account_create_handler, sender=UserAccount)
post_save.connect(user_follow_handler, sender=UserAccount)