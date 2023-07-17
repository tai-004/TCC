# Generated by Django 4.0.8 on 2023-02-21 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0026_remove_instituicao_bairroadm_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='dtaDeFuncaoAdm',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='dtaDenascAdm',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='emailAdm',
            field=models.EmailField(default='Email do Adiministrador', max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='funcaoAdm',
            field=models.CharField(default='Função do Administrador na instituição', max_length=100, null=True),
        ),
    ]