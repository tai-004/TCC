# Generated by Django 4.0.8 on 2023-06-02 00:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('voluntariado', '0028_remove_curriculo_sender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curriculo',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
