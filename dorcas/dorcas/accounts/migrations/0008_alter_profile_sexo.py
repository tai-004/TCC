# Generated by Django 4.0.8 on 2023-01-10 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_remove_profile_responsavel_profile_responsavel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='sexo',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]