# Generated by Django 2.2.1 on 2019-06-01 23:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='departament',
            new_name='department',
        ),
    ]