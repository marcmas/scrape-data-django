# Generated by Django 3.0.1 on 2020-01-02 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificate', '0006_auto_20200101_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='signature',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]