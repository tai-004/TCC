# Generated by Django 4.0.8 on 2023-07-13 01:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0089_instituicao_banner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instituicao',
            name='banner',
        ),
    ]