# Generated by Django 4.0.8 on 2023-07-16 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noti', '0023_tabela_notis_lido'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificacao',
            name='apresentar',
            field=models.BooleanField(default=False),
        ),
    ]