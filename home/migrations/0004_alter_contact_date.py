# Generated by Django 3.2.4 on 2021-06-27 05:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_contact_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 6, 27, 5, 23, 28, 463740, tzinfo=utc)),
        ),
    ]