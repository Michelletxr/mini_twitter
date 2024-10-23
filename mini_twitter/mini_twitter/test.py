from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from post.models import Post

User = get_user_model()

class PostTests(APITestCase):
    
    def setUp(self):
        # Criação de um usuário de teste
        self.user = User.objects.create_user(username="testuser", password="testpass")
        
        # Criação de alguns posts
        self.post1 = Post.objects.create(user=self.user, content="Post 1")
        self.post2 = Post.objects.create(user=self.user, content="Post 2")
        
        # Autenticação do cliente
        self.client = APIClient()
        self.client.login(username="testuser", password="testpass")

    def test_get_posts_authenticated(self):
        """Testa se um usuário autenticado pode obter a lista de posts."""
        
        # Faz uma requisição GET para o endpoint de posts
        url = reverse('post:post-list')  # Nome da URL
        response = self.client.get(url)

        # Verifica se o status HTTP é 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.data['results']
        # Verifica se os dados retornados têm a quantidade correta de posts
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]['content'], 'Post 1')
        self.assertEqual(data[1]['content'], 'Post 2')