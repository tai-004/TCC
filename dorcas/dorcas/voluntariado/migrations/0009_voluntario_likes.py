# Generated by Django 4.0.8 on 2023-03-21 00:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('voluntariado', '0008_blogpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='voluntario',
            name='likes',
            field=models.ManyToManyField(related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
