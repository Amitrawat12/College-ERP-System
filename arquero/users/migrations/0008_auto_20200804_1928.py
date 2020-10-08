# Generated by Django 3.0.5 on 2020-08-04 13:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20200804_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_attendance',
            name='Attendance',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='student_attendance',
            name='Roll_no',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='student_attendance',
            name='subject',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teacher_attendance',
            name='Sign_in',
            field=models.TimeField(default=datetime.datetime(2020, 8, 4, 19, 28, 12, 692385)),
        ),
    ]
