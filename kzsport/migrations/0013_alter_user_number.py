# Generated by Django 4.0.2 on 2022-04-14 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kzsport', '0012_alter_user_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='number',
            field=models.BigIntegerField(),
        ),
    ]