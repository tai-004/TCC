# Generated by Django 4.0.8 on 2023-04-22 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0059_rename_user_instituicao_autor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='instituicao',
            old_name='autor',
            new_name='user',
        ),
    ]