# Generated by Django 4.1 on 2022-08-25 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_trait_disc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trait',
            name='disc',
            field=models.CharField(max_length=900, verbose_name='Description'),
        ),
    ]
