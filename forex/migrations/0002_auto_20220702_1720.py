# Generated by Django 3.2.13 on 2022-07-02 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forex', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reporthistoryprediction',
            name='predicted_hit_high',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='reporthistoryprediction',
            name='predicted_hit_low',
            field=models.DateTimeField(null=True),
        ),
    ]