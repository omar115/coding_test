# Generated by Django 3.2.8 on 2021-10-18 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_childuser_parent_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='childuser',
            name='parent_user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.parentuser'),
        ),
    ]
