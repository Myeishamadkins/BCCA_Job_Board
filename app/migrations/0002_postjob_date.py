# Generated by Django 2.1.7 on 2019-03-29 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postjob',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]