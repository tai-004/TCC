# Generated by Django 4.0.8 on 2023-06-22 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('responsavel', '0014_alter_responsavel_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='responsavel',
            name='telefone',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]