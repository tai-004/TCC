# Generated by Django 4.0.8 on 2023-04-08 22:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('responsavel', '0008_m'),
    ]

    operations = [
        migrations.RenameField(
            model_name='responsavel',
            old_name='author',
            new_name='user',
        ),
    ]