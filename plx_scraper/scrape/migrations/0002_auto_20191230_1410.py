# Generated by Django 3.0.1 on 2019-12-30 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrape', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='path',
            name='path',
            field=models.CharField(default='C:/Users/MarcinPC/Desktop/kinter/direcories', max_length=200),
        ),
    ]
