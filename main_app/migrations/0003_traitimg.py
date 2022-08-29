# Generated by Django 4.1 on 2022-08-29 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_comp_desc_comp_imgfive_comp_imgfour_comp_imgone_and_more'),
    ]

    operations = [
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