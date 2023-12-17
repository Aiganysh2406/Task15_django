# Generated by Django 5.0 on 2023-12-17 05:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0002_microorganisms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bacteria',
            name='properties',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='fungi',
            name='properties',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='microorganisms',
            name='bacteria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.bacteria'),
        ),
        migrations.AlterField(
            model_name='microorganisms',
            name='fungi',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='MyApp.fungi'),
        ),
        migrations.AlterField(
            model_name='microorganisms',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]