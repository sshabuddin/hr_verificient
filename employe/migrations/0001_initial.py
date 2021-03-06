# Generated by Django 3.0.3 on 2020-02-29 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employe',
            fields=[
                ('emp_id', models.IntegerField(primary_key=True, serialize=False)),
                ('emp_name', models.CharField(max_length=50)),
                ('phonenumber', models.IntegerField()),
                ('joining_date', models.DateTimeField()),
                ('emp_email', models.CharField(max_length=50)),
                ('reporting_manager', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'employe',
            },
        ),
    ]
