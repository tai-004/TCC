# Generated by Django 4.0.8 on 2023-03-18 04:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noti', '0002_notifications_noti'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notifications',
            old_name='voluntariado',
            new_name='voluntario',
        ),
    ]
