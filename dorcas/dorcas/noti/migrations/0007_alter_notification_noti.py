# Generated by Django 4.0.8 on 2023-04-16 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noti', '0006_alter_notification_noti'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='noti',
            field=models.IntegerField(blank=True, choices=[(1, 'Like'), (2, 'Volu')], null=True),
        ),
    ]
