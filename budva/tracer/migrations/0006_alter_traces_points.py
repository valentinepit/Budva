# Generated by Django 4.0.6 on 2022-07-10 18:04

from django.db import migrations
import sortedm2m.fields


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0002_alter_points_options'),
        ('tracer', '0005_alter_traces_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traces',
            name='points',
            field=sortedm2m.fields.SortedManyToManyField(help_text=None, to='points.points'),
        ),
    ]
