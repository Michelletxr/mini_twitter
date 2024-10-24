import os
import django
from post.models import Post
from django.contrib.auth import get_user_model

# Configurações do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mini_twitter.settings')
django.setup()

# Obter o modelo de usuário customizado
User = get_user_model()

# Função para criar 10 posts
def create_posts():
    # Obtenha um usuário autor existente (ou crie um usuário fictício)
    user = User.objects.first()  # Use o primeiro usuário existente como autor
    for i in range(1, 11):
        post_content = f"Este é o conteúdo do post número {i}."
        Post.objects.create(user=user, content=post_content,  )
        print(f"Post {i} criado com sucesso!")


create_posts()
