# Generated by Django 2.1.2 on 2018-10-06 22:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='album',
            fields=[
                ('album_id', models.AutoField(primary_key=True, serialize=False)),
                ('album_title', models.CharField(max_length=250)),
                ('artist', models.CharField(max_length=250)),
                ('genre', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='song',
            fields=[
                ('song_id', models.AutoField(primary_key=True, serialize=False)),
                ('file_type', models.CharField(max_length=20)),
                ('song_title', models.CharField(max_length=250)),
                ('song_album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musiclibrary.album')),
            ],
        ),
    ]
