# Generated by Django 3.0.4 on 2020-04-19 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='name',
            field=models.CharField(default='lagos', max_length=25),
            preserve_default=False,
        ),
    ]
