# Generated by Django 4.0.8 on 2023-04-18 01:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('instituicao', '0006_remove_tabela_sender_remove_tabela_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tabela',
            name='meu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='donodoperfil', to=settings.AUTH_USER_MODEL),
        ),
    ]