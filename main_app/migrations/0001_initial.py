# Generated by Django 4.1 on 2022-08-29 22:01

from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Augment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('tier', models.IntegerField()),
                ('desc', models.CharField(max_length=900, verbose_name='Description')),
                ('icon', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Champion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ability', models.CharField(max_length=500)),
                ('abilname', models.CharField(max_length=100)),
                ('abilicon', models.CharField(max_length=100)),
                ('cost', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('icon', models.CharField(max_length=100)),
                ('armor', models.IntegerField()),
                ('attack_speed', models.DecimalField(decimal_places=2, max_digits=3, verbose_name='Attack Speed')),
                ('damage', models.CharField(max_length=100, verbose_name='Damage')),
                ('hp', models.CharField(max_length=100, verbose_name='Health')),
                ('initialmana', models.CharField(max_length=100, verbose_name='Mana')),
                ('magic_resist', models.IntegerField(verbose_name='Magic Resist')),
                ('range', models.IntegerField()),
                ('traits', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Comp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('tier', models.CharField(max_length=500)),
                ('desc', models.CharField(max_length=500)),
                ('imgone', models.CharField(max_length=500)),
                ('imgtwo', models.CharField(max_length=500)),
                ('imgthree', models.CharField(max_length=500)),
                ('imgfour', models.CharField(max_length=500)),
                ('imgfive', models.CharField(max_length=500)),
                ('imgsix', models.CharField(max_length=500)),
                ('imgseven', models.CharField(max_length=500)),
                ('nameone', models.CharField(max_length=500)),
                ('nametwo', models.CharField(max_length=500)),
                ('namethree', models.CharField(max_length=500)),
                ('namefour', models.CharField(max_length=500)),
                ('namefive', models.CharField(max_length=500)),
                ('namesix', models.CharField(max_length=500)),
                ('nameseven', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Trait',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('desc', models.CharField(max_length=900, verbose_name='Description')),
                ('icon', models.CharField(max_length=100)),
                ('champions', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('url', embed_video.fields.EmbedVideoField()),
            ],
        ),
        migrations.CreateModel(
            name='Traitimg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charname', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='main_app/static/images/home')),
                ('charimage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='traitimage', to='main_app.trait')),
            ],
        ),
    ]
