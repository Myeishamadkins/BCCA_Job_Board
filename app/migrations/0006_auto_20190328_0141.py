# Generated by Django 2.1.7 on 2019-03-28 01:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20190315_1635'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='post_job',
        ),
        migrations.DeleteModel(
            name='Application',
        ),
    ]