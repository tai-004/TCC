# Generated by Django 4.0.8 on 2023-04-17 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instituicao', '0003_rename_table_aceite_tabela'),
    ]

    operations = [
        migrations.AddField(
            model_name='tabela',
            name='cnt',
            field=models.IntegerField(default=0),
        ),
    ]
