# Generated by Django 4.0.8 on 2023-02-23 23:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('responsavel', '0005_responsavel_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='responsavel',
            name='author',
        ),
    ]
