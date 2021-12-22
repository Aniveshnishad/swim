# Generated by Django 3.1.1 on 2021-03-30 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_otp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentprofile',
            old_name='parent_name',
            new_name='father_name',
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='mother_name',
            field=models.CharField(default='asa', max_length=300),
            preserve_default=False,
        ),
    ]