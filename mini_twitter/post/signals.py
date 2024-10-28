from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Post
from mini_twitter.utils import send_custom_email



@receiver(post_save, sender=Post)
def post_receive_like_handler(sender, instance: Post, created, **kwargs):
    if 'likes_count' in kwargs['update_fields']:
        user = instance.user
        message = f'HELLO! {user.username} Post receive likes!'
        subject = 'Post receive likes'
        to_user = user.email
        send_custom_email(subject, message, [to_user])

post_save.connect(post_receive_like_handler, sender=Post)