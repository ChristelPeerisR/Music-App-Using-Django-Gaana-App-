# Generated by Django 4.2.7 on 2023-11-21 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gaanaapp', '0003_remove_artist_artists_file_remove_top_top_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thumb_fr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumb1_img', models.ImageField(upload_to='pics')),
            ],
        ),
        migrations.CreateModel(
            name='Thumb_sn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumb2_img', models.ImageField(upload_to='pics')),
            ],
        ),
        migrations.CreateModel(
            name='Thumb_tr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumb3_img', models.ImageField(upload_to='pics')),
            ],
        ),
    ]
