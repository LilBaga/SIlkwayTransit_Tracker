# Generated by Django 4.1.1 on 2022-09-18 03:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0004_stations_remove_mash_accept_train_time_begin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stations',
            name='stations',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]