# Generated by Django 4.1.6 on 2023-02-23 21:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letterapp', '0009_alter_letter_sendat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letter',
            name='sendAt',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 23, 21, 18, 21, 721796)),
        ),
    ]
