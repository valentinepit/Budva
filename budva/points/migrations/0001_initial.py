# Generated by Django 4.0.6 on 2022-07-10 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Points',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('abscissa', models.FloatField(verbose_name='x')),
                ('ordinata', models.FloatField(verbose_name='y')),
            ],
            options={
                'ordering': ['abscissa'],
            },
        ),
    ]
