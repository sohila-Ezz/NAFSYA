# Generated by Django 3.2.4 on 2021-07-13 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docters', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docter',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
