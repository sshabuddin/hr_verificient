# Generated by Django 2.2.6 on 2020-03-01 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employe',
            name='joining_date',
            field=models.DateField(),
        ),
    ]
