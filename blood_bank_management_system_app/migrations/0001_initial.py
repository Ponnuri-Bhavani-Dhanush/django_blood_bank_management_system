# Generated by Django 3.1.7 on 2022-08-15 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fname', models.CharField(max_length=20)),
                ('Lname', models.CharField(max_length=20)),
                ('age', models.IntegerField(null=True)),
                ('Gender', models.CharField(max_length=10)),
                ('Mobile', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('group', models.CharField(max_length=4)),
            ],
            options={
                'db_table': 'demo_blood',
            },
        ),
    ]
