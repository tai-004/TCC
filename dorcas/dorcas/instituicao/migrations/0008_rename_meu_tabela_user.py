# Generated by Django 4.0.8 on 2023-04-18 01:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instituicao', '0007_tabela_meu'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tabela',
            old_name='meu',
            new_name='user',
        ),
    ]