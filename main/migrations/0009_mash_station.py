# Generated by Django 4.1.1 on 2022-09-18 04:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_mash_station1'),
    ]

    operations = [
        migrations.AddField(
            model_name='mash',
            name='station',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.stations'),
        ),
    ]