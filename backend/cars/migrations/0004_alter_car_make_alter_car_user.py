# Generated by Django 4.1.7 on 2023-02-19 19:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cars', '0003_remove_car_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='make',
            field=models.CharField(blank=True, default='Volvo', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='user',
            field=models.ForeignKey(default='admin', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
