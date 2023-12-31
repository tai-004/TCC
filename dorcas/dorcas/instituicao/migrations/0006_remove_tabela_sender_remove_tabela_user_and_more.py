# Generated by Django 4.0.8 on 2023-04-18 01:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('noti', '0011_rename_tabelanoti_tabela_notis'),
        ('instituicao', '0005_remove_tabela_cnt_tabela_sender_alter_tabela_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tabela',
            name='sender',
        ),
        migrations.RemoveField(
            model_name='tabela',
            name='user',
        ),
        migrations.RemoveField(
            model_name='tabela',
            name='voluntario',
        ),
        migrations.AddField(
            model_name='tabela',
            name='notificacao',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='donodoperfil', to='noti.notification'),
        ),
    ]
