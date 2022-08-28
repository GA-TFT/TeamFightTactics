# Generated by Django 4.1 on 2022-08-28 20:48

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_remove_champion_initialmama_remove_champion_mana_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('url', embed_video.fields.EmbedVideoField()),
            ],
        ),
    ]