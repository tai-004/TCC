# Generated by Django 4.0.8 on 2023-04-17 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voluntariado', '0014_remove_voluntario_likes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='voluntario',
            old_name='likes_count',
            new_name='aceitar_count',
        ),
    ]