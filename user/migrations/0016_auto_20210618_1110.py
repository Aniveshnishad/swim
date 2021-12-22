# Generated by Django 3.1.1 on 2021-06-18 11:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_weektimeslots'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='weektimeslots',
            options={'verbose_name': 'Weekly break Time', 'verbose_name_plural': 'Weekly break Time'},
        ),
        migrations.AlterField(
            model_name='weektimeslots',
            name='friday_endTime_slot',
            field=models.TimeField(default=django.utils.timezone.now, error_messages={'error': 'Choose a valid time format.'}, help_text='Choose friday start break time slot or set it current time.', verbose_name='Friday break time end'),
        ),
        migrations.AlterField(
            model_name='weektimeslots',
            name='friday_startTime_slot',
            field=models.TimeField(default=django.utils.timezone.now, error_messages={'error': 'Choose a valid time format.'}, help_text='Choose friday start break time slot or set it current time.', verbose_name='Friday break time start'),
        ),
        migrations.AlterField(
            model_name='weektimeslots',
            name='monday_endTime_slot',
            field=models.TimeField(default=django.utils.timezone.now, error_messages={'error': 'Choose a valid time format.'}, help_text='Choose monday start break time slot or set it current time.', verbose_name='Monday break time end'),
        ),
        migrations.AlterField(
            model_name='weektimeslots',
            name='monday_startTime_slot',
            field=models.TimeField(default=django.utils.timezone.now, error_messages={'error': 'Choose a valid time format.'}, help_text='Choose monday start break time slot or set it current time.', verbose_name='Monday break time start'),
        ),
        migrations.AlterField(
            model_name='weektimeslots',
            name='saturday_endTime_slot',
            field=models.TimeField(default=django.utils.timezone.now, error_messages={'error': 'Choose a valid time format.'}, help_text='Choose saturday start break time slot or set it current time.', verbose_name='Saturday break time end'),
        ),
        migrations.AlterField(
            model_name='weektimeslots',
            name='saturday_startTime_slot',
            field=models.TimeField(default=django.utils.timezone.now, error_messages={'error': 'Choose a valid time format.'}, help_text='Choose saturday start break time slot or set it current time.', verbose_name='Saturday break time start'),
        ),
        migrations.AlterField(
            model_name='weektimeslots',
            name='sunday_endTime_slot',
            field=models.TimeField(default=django.utils.timezone.now, error_messages={'error': 'Choose a valid time format.'}, help_text='Choose sunday start break time slot or set it current time.', verbose_name='Sunday break time end'),
        ),
        migrations.AlterField(
            model_name='weektimeslots',
            name='sunday_startTime_slot',
            field=models.TimeField(default=django.utils.timezone.now, error_messages={'error': 'Choose a valid time format.'}, help_text='Choose sunday start break time slot or set it current time.', verbose_name='Sunday break time start'),
        ),
        migrations.AlterField(
            model_name='weektimeslots',
            name='thursday_endTime_slot',
            field=models.TimeField(default=django.utils.timezone.now, error_messages={'error': 'Choose a valid time format.'}, help_text='Choose thursday start break time slot or set it current time.', verbose_name='Thursday break time end'),
        ),
        migrations.AlterField(
            model_name='weektimeslots',
            name='thursday_startTime_slot',
            field=models.TimeField(default=django.utils.timezone.now, error_messages={'error': 'Choose a valid time format.'}, help_text='Choose thursday start break time slot or set it current time.', verbose_name='Thursday break time start'),
        ),
        migrations.AlterField(
            model_name='weektimeslots',
            name='tuesday_endTime_slot',
            field=models.TimeField(default=django.utils.timezone.now, error_messages={'error': 'Choose a valid time format.'}, help_text='Choose tuesday start break time slot or set it current time.', verbose_name='Tuesday break time end'),
        ),
        migrations.AlterField(
            model_name='weektimeslots',
            name='tuesday_startTime_slot',
            field=models.TimeField(default=django.utils.timezone.now, error_messages={'error': 'Choose a valid time format.'}, help_text='Choose tuesday start break time slot or set it current time.', verbose_name='Tuesday break time start'),
        ),
        migrations.AlterField(
            model_name='weektimeslots',
            name='wednesday_endTime_slot',
            field=models.TimeField(default=django.utils.timezone.now, error_messages={'error': 'Choose a valid time format.'}, help_text='Choose wednesday start break time slot or set it current time.', verbose_name='Wednesday break time end'),
        ),
        migrations.AlterField(
            model_name='weektimeslots',
            name='wednesday_startTime_slot',
            field=models.TimeField(default=django.utils.timezone.now, error_messages={'error': 'Choose a valid time format.'}, help_text='Choose wednesday start break time slot or set it current time.', verbose_name='Wednesday break time start'),
        ),
    ]