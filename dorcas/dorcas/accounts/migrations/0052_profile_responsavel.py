# Generated by Django 4.0.8 on 2023-04-08 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('responsavel', '0008_m'),
        ('accounts', '0051_remove_profile_responsavel'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='responsavel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='responsavel.responsavel'),
        ),
    ]
