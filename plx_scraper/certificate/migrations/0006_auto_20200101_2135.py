# Generated by Django 3.0.1 on 2020-01-01 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('certificate', '0005_auto_20191231_1224'),
    ]

    operations = [
        migrations.RenameField(
            model_name='certificate',
            old_name='laeve_date',
            new_name='leave_date',
        ),
    ]