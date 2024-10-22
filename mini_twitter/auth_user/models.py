
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

# Create your models here.

class UserAccount(AbstractUser):
    # O campo para seguir outros usuários
    followers = models.ManyToManyField('self', symmetrical=False, verbose_name='followers', related_name='following', blank=True)
    first_name = models.CharField(verbose_name='first name', max_length=30)
    last_name = models.CharField(verbose_name='last name', max_length=150)
    email = models.EmailField(verbose_name='email address', unique=True)
    date_of_birth = models.DateField(verbose_name='birthdate')

    groups = models.ManyToManyField(
        Group,
        related_name='user_account_set',  # Definindo um related_name único para evitar conflitos
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='user_account_permissions_set',  # Definindo um related_name único para evitar conflitos
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )

    class Meta:
        verbose_name = "Account User"

    def __str__(self):
        return f"User {self.username} account"
    

    def follow(self, user):
        """Segue um usuário."""
        self.following.add(user)

    def unfollow(self, user):
        """Deixa de seguir um usuário."""
        self.following.remove(user)

