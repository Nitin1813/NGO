# Generated by Django 3.1.2 on 2021-05-12 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('Amount', models.IntegerField(max_length=200)),
                ('Date', models.DateField()),
                ('Time', models.TimeField()),
                ('Phone', models.IntegerField(max_length=10)),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
    ]
