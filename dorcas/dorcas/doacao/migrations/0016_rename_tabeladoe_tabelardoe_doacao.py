# Generated by Django 4.0.8 on 2023-05-28 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doacao', '0015_remove_doeuser_sender_doeuser_sender_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tabelardoe',
            old_name='tabelaDoe',
            new_name='doacao',
        ),
    ]