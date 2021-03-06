# Generated by Django 4.0.6 on 2022-07-10 17:21

from django.db import migrations
import sortedm2m.fields


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0002_alter_points_options'),
        ('tracer', '0003_traces_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traces',
            name='points',
            field=sortedm2m.fields.SortedManyToManyField(blank=True, help_text=None, related_name='included_points', to='points.points'),
        ),
    ]
