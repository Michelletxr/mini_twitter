import os
import django
from faker import Faker
from random import choice, randint
from auth_user.models import UserAccount
from post.models import Post

# Configurações do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mini_twitter.settings')
django.setup()

fake = Faker()

def populate_posts(n=200):
    users = list(UserAccount.objects.all())

    for _ in range(n):
        user = choice(users)
        content = fake.text(max_nb_chars=280)  # Limite de 280 caracteres como o Twitter
        likes_count = randint(0, 100)  # Número aleatório de likes entre 0 e 100
        
        post = Post.objects.create(
            user=user,
            content=content,
            likes_count=likes_count,
            is_deleted=False)


