# Generated by Django 5.1.2 on 2024-10-25 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('auth_user', '0007_alter_useraccount_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='user_account_set', to='auth.group', verbose_name='groups'),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, related_name='user_account_permissions_set', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
