# Generated by Django 4.0.8 on 2023-05-21 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('voluntariado', '0024_curriculo'),
        ('noti', '0018_tabela_notis_curriculo_remove_tabela_notis_sender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tabela_notis',
            name='curriculo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notiCurriculo', to='voluntariado.curriculo'),
        ),
    ]
