# Generated by Django 3.0.8 on 2020-08-06 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='birth',
        ),
        migrations.AddField(
            model_name='customuser',
            name='class_code',
            field=models.CharField(blank=True, max_length=9, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='major',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]