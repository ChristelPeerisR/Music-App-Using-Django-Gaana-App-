# Generated by Django 4.2.7 on 2023-11-21 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gaanaapp', '0004_thumb_fr_thumb_sn_thumb_tr'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='artists_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recent',
            name='recent_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='top',
            name='top_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trend',
            name='trend_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]