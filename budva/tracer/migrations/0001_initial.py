# Generated by Django 4.0.6 on 2022-07-10 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('points', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Traces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('distance', models.FloatField(verbose_name='Distance')),
                ('trace', models.CharField(max_length=20)),
                ('points', models.ManyToManyField(blank=True, related_name='included_points', to='points.points')),
            ],
        ),
    ]
