# Generated by Django 4.2.7 on 2023-11-22 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gaanaapp', '0007_remove_artist_artists_id_remove_recent_recent_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recent',
            name='artists_name',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trend',
            name='artists_name',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
