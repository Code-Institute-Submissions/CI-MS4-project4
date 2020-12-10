# Generated by Django 3.1.4 on 2020-12-09 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('cost', models.FloatField()),
                ('unit', models.CharField(max_length=10)),
                ('quantity', models.IntegerField(default=0)),
                ('part_number', models.CharField(max_length=15)),
                ('desc', models.TextField()),
            ],
        ),
    ]