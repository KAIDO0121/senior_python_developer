# Generated by Django 4.0.2 on 2022-02-12 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coffee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bean_from', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=50)),
            ],
        ),
    ]
