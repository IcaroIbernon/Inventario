# Generated by Django 3.0.3 on 2020-03-14 23:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cartas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventario',
            old_name='Done',
            new_name='Dono',
        ),
    ]