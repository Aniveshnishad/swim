# Generated by Django 3.1.1 on 2021-06-19 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0017_breaktime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breaktime',
            name='week_day',
            field=models.CharField(choices=[('1', 'monday'), ('2', 'tuesday'), ('3', 'wednesday'), ('4', 'thursday'), ('5', 'friday'), ('6', 'saturday'), ('7', 'sunday')], max_length=1),
        ),
    ]
