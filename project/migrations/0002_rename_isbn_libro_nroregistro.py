# Generated by Django 4.2.2 on 2023-07-03 02:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='libro',
            old_name='isbn',
            new_name='nroregistro',
        ),
    ]
