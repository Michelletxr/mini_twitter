from celery import shared_task
from mini_twitter.utils import send_custom_email
from .models import UserAccount
from datetime import datetime

data_atual = datetime.now().date()

@shared_task
def send_email_birthdate(data_username):
    user = UserAccount.objects.get(username=data_username)
    if user.date_of_birth == data_atual:
        message = f'Happy birthday {user.username}!'
        subject = 'Happy birthday'
        to_user = user.email
        print(f'Request: {data_username}')
        print("Data atual| data user", data_atual, user.date_of_birth)
        send_custom_email(subject, message, [to_user])