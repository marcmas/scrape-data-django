# Generated by Django 3.0.1 on 2019-12-30 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrape', '0004_auto_20191230_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='path',
            field=models.CharField(default='path', max_length=200),
        ),
    ]