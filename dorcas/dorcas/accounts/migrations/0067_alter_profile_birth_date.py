# Generated by Django 4.0.8 on 2023-04-29 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0066_idade_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
