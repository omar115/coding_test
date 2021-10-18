# Generated by Django 3.2.8 on 2021-10-18 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20211018_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='childuser',
            name='child_first_name',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Child First Name'),
        ),
        migrations.AlterField(
            model_name='childuser',
            name='child_last_name',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Child Last Name'),
        ),
        migrations.AlterField(
            model_name='parentuser',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='City Name'),
        ),
        migrations.AlterField(
            model_name='parentuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Parent First Name'),
        ),
        migrations.AlterField(
            model_name='parentuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Parent Last Name'),
        ),
        migrations.AlterField(
            model_name='parentuser',
            name='state',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='State Name'),
        ),
        migrations.AlterField(
            model_name='parentuser',
            name='street',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Street Address'),
        ),
        migrations.AlterField(
            model_name='parentuser',
            name='zip_code',
            field=models.IntegerField(blank=True, null=True, verbose_name='Zip Code'),
        ),
    ]
