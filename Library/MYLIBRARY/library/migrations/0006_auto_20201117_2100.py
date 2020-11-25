# Generated by Django 3.1.3 on 2020-11-17 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_auto_20201117_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Date_of_Birth',
            field=models.DateField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.TextField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='profile',
            name='adhar_card',
            field=models.IntegerField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='profile',
            name='borrow_date',
            field=models.DateField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email_id',
            field=models.EmailField(blank=True, default=None, max_length=254),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='return_date',
            field=models.DateField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='profile',
            name='town',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]