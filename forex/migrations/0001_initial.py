# Generated by Django 3.2.13 on 2022-06-30 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReportHistoryPrediction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_id', models.CharField(max_length=200)),
                ('currency', models.CharField(max_length=20)),
                ('interval', models.CharField(max_length=200)),
                ('prediction_high', models.BigIntegerField()),
                ('prediction_low', models.BigIntegerField()),
                ('target_datetime', models.DateTimeField()),
                ('predicted_hit_high', models.DateTimeField()),
                ('predicted_hit_low', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ReportStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_id', models.CharField(max_length=200)),
                ('status', models.IntegerField()),
                ('comment', models.TextField(max_length=200)),
                ('user_id', models.CharField(max_length=200)),
            ],
        ),
    ]
