# Generated by Django 4.0.8 on 2023-05-05 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noti', '0014_aceitar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aceitar',
            old_name='voluntario',
            new_name='notificacao',
        ),
    ]
