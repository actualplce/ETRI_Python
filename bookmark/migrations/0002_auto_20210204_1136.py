# Generated by Django 3.1.6 on 2021-02-04 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='title',
            field=models.CharField(blank=True, max_length=100, verbose_name='TITLE'),
        ),
    ]