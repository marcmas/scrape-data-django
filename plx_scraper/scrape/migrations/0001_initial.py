# Generated by Django 3.0.1 on 2019-12-30 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('column_one', models.CharField(default='PLX', max_length=50)),
                ('column_two', models.CharField(default='PLX_FGK', max_length=50)),
                ('file_name', models.CharField(blank=True, max_length=50, null=True)),
                ('column_three', models.CharField(default='N', max_length=50)),
                ('column_four', models.CharField(default='1', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Path',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(blank=True, default='C:/Users/MarcinPC/Desktop/kinter/direcories', max_length=200, null=True)),
            ],
        ),
    ]