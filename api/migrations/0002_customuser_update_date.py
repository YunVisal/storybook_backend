# Generated by Django 4.2 on 2024-01-26 01:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='update_date',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]
