# Generated by Django 3.1.3 on 2020-11-22 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0013_auto_20201120_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Number_of_copies',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='book_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
