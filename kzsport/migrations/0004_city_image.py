# Generated by Django 4.0.2 on 2022-03-16 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kzsport', '0003_food_rename_traditions_tradition_delete_foods'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='image',
            field=models.CharField(default='0000000', max_length=200),
        ),
    ]