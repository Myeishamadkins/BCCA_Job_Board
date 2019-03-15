# Generated by Django 2.1.7 on 2019-03-15 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_application'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('comment', models.TextField()),
                ('post_comment', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.PostJob')),
            ],
        ),
    ]