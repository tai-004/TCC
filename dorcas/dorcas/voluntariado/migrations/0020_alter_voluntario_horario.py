# Generated by Django 4.0.8 on 2023-05-04 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voluntariado', '0019_delete_blogpost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voluntario',
            name='horario',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
