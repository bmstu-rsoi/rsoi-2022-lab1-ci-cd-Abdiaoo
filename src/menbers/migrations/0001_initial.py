# Generated by Django 4.1.1 on 2022-09-20 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('age', models.IntegerField()),
                ('adresse', models.CharField(max_length=300)),
                ('work', models.CharField(max_length=300)),
            ],
        ),
    ]
