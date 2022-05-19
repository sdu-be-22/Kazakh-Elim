# Generated by Django 4.0.2 on 2022-04-12 14:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('kzsport', '0009_delete_writer'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='age',
            field=models.IntegerField(default=18),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='feedback',
            name='email',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='feedback',
            name='rate',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='feedback',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
