# Generated by Django 4.0.8 on 2023-05-04 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0070_delete_idade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instituicao',
            name='bio',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
