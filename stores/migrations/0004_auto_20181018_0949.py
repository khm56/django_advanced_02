# Generated by Django 2.0.7 on 2018-10-18 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0003_auto_20181018_0929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
