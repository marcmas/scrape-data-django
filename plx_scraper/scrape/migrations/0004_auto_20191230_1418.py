# Generated by Django 3.0.1 on 2019-12-30 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scrape', '0003_files_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='path',
            field=models.ForeignKey(default='C:/Users/MarcinPC/Desktop/kinter/direcories', on_delete=django.db.models.deletion.CASCADE, to='scrape.Path'),
        ),
    ]
