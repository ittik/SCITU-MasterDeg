# Generated by Django 2.0.2 on 2018-04-29 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='reg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('date', models.DateField()),
                ('content', models.TextField(max_length=5000)),
                ('file', models.FileField(blank=True, upload_to='')),
            ],
        ),
    ]
