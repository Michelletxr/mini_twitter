
from django.contrib.auth.models import Group, Permission
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        """Cria e salva um usuário com o email e senha especificados."""
        if not username:
            raise ValueError('O usuário deve ter um username.')
        if not email:
            raise ValueError('O usuário deve ter um endereço de email.')
        
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password=None, **extra_fields):
        """cria superusuário."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, password, **extra_fields)

class UserAccount(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    followers = models.ManyToManyField('self', symmetrical=False, verbose_name='followers', related_name='following', blank=True)
    first_name = models.CharField(verbose_name='first name', max_length=30)
    last_name = models.CharField(verbose_name='last name', max_length=150)
    email = models.EmailField(verbose_name='email address', unique=True)
    date_of_birth = models.DateField(verbose_name='birthdate', null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()
    REQUIRED_FIELDS = ['email']
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'

    groups = models.ManyToManyField(
        Group,
        related_name='user_account_set',
        blank=True,
        verbose_name="groups",
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='user_account_permissions_set',
        blank=True,
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

