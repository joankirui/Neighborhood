# Generated by Django 3.2.9 on 2022-01-06 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighborapp', '0002_auto_20220106_2323'),
    ]

    operations = [
        migrations.AddField(
            model_name='neighborhood',
            name='health_tell',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='neighborhood',
            name='police_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
