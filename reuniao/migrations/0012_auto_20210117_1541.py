# Generated by Django 3.1.5 on 2021-01-17 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reuniao', '0011_auto_20210117_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reuniao',
            name='ausente',
            field=models.CharField(choices=[('presente', 'Presente'), ('ausente', 'Ausente')], max_length=8, null=True),
        ),
    ]
