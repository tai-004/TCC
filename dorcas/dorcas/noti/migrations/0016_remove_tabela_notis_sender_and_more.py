# Generated by Django 4.0.8 on 2023-05-05 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noti', '0015_rename_voluntario_aceitar_notificacao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tabela_notis',
            name='sender',
        ),
        migrations.RemoveField(
            model_name='tabela_notis',
            name='tabela',
        ),
        migrations.RemoveField(
            model_name='tabela_notis',
            name='user',
        ),
        migrations.DeleteModel(
            name='Aceitar',
        ),
        migrations.DeleteModel(
            name='Tabela_notis',
        ),
    ]