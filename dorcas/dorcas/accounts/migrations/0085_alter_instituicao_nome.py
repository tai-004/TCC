# Generated by Django 4.0.8 on 2023-06-19 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0084_remove_profile_bairro_remove_profile_cidade_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instituicao',
            name='nome',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
