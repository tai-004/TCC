# Generated by Django 4.0.8 on 2023-02-21 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0035_alter_profile_dtadefuncaoadm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dtaDenascAdm',
            field=models.CharField(blank=True, default='00/00/0000', max_length=100, null=True),
        ),
    ]
