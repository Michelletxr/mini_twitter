import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mini_twitter.settings')
django.setup()

from faker import Faker
from random import randint
from auth_user.models import UserAccount

fake = Faker()

def populate_users(n=100):
    for _ in range(n):
        username = fake.unique.user_name()
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.unique.email()
        date_of_birth = fake.date_of_birth(minimum_age=18, maximum_age=90)
        
        # Cria um novo usuário
        user = UserAccount.objects.create_user(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            password='defaultpassword123'  # Use uma senha padrão ou gere aleatoriamente
        )
        
        # Adiciona seguidores aleatórios
        followers_count = randint(0, 10)  # Define até 10 seguidores aleatórios por usuário
        follower_ids = UserAccount.objects.order_by('?').values_list('id', flat=True)[:followers_count]
        user.followers.set(follower_ids)
        
        print(f"Usuário {username} criado com {followers_count} seguidores.")


print("Populando o banco de dados com usuários...")
populate_users(100)
print("População de usuários concluída com sucesso!")
