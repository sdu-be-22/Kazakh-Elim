# Generated by Django 3.2.10 on 2022-05-02 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kzsport', '0019_delete_tradition'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tradition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Atau')),
                ('intro', models.CharField(max_length=250, verbose_name='Anons')),
                ('full_text', models.TextField(verbose_name='Sipat')),
                ('famous', models.CharField(max_length=40, verbose_name='Name')),
                ('history', models.TextField(verbose_name='Tarih')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
        ),
    ]
