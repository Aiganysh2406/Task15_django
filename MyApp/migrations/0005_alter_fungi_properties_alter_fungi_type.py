# Generated by Django 5.0 on 2023-12-17 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0004_alter_microorganisms_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fungi',
            name='properties',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='fungi',
            name='type',
            field=models.CharField(max_length=250),
        ),
    ]
