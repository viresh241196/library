# Generated by Django 3.1.3 on 2020-11-23 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0016_auto_20201122_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Date_of_Birth',
            field=models.CharField(blank=True, default=0, max_length=50, null=True),
        ),
    ]
