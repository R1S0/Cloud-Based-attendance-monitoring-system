# Generated by Django 4.0.3 on 2022-03-11 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0006_remove_student_student_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_code',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
