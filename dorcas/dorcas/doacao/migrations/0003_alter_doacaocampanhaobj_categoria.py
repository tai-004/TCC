# Generated by Django 4.0.8 on 2023-05-27 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doacao', '0002_doacaocampanhaobj_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doacaocampanhaobj',
            name='categoria',
            field=models.CharField(choices=[['material de limpeza', 'material de limpeza'], ['roupa', 'roupa'], ['brinquedo', 'brinquedo'], ['outros', 'outros']], max_length=100, null=True),
        ),
    ]