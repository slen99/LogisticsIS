# Generated by Django 2.0.2 on 2018-10-27 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Berth',
            fields=[
                ('berth_name', models.CharField(max_length=50)),
                ('berth_id', models.IntegerField(primary_key=True, serialize=False)),
                ('berth_cap', models.IntegerField(default=20, editable=False)),
                ('berth_used', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ship',
            fields=[
                ('ship_id', models.IntegerField(primary_key=True, serialize=False)),
                ('ship_name', models.CharField(max_length=50)),
                ('is_anchored', models.BooleanField(default=True)),
                ('ship_manager', models.CharField(max_length=20)),
            ],
        ),
    ]
