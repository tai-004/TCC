# Generated by Django 4.0.8 on 2023-06-02 01:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voluntariado', '0031_alter_curriculo_user_alter_curriculo_user2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curriculo',
            name='user2',
        ),
    ]