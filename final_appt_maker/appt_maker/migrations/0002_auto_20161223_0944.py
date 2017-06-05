# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appt_maker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointments',
            name='time',
            field=models.TimeField(verbose_name=b'Time of Appointment '),
        ),
    ]
