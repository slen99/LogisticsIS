# Generated by Django 2.0.2 on 2018-12-27 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipmanage', '0012_auto_20181220_0028'),
    ]

    operations = [
        migrations.AddField(
            model_name='ship',
            name='ship_photo',
            field=models.ImageField(default=20, height_field='url_height', upload_to='icons', width_field='url_width'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(default='201812280015549040', editable=False, max_length=18, primary_key=True, serialize=False),
        ),
    ]
