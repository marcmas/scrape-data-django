# Generated by Django 3.0.1 on 2019-12-31 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('certificate', '0004_auto_20191231_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='certificate.Profile'),
        ),
    ]