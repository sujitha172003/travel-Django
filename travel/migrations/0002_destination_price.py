# Generated by Django 5.0.3 on 2024-04-30 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='price',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
