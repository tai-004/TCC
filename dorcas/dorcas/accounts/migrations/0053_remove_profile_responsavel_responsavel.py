# Generated by Django 4.0.8 on 2023-04-16 02:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('responsavel', '0010_remove_responsavel_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0052_profile_responsavel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='responsavel',
        ),
        migrations.CreateModel(
            name='responsavel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('responsavel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='responsavel.responsavel')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]