# Generated by Django 3.2.9 on 2022-01-06 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('neighborapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=60)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hood', to='neighborapp.profile')),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='neighborhood',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='members', to='neighborapp.neighborhood'),
        ),
    ]
