# Generated by Django 3.1.5 on 2021-01-15 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CodigoAcceso',
            fields=[
                ('codigo', models.IntegerField()),
                ('usuario', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('registro', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SensorEstanque',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=20)),
                ('modelo', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=20)),
                ('nivel', models.CharField(max_length=5)),
                ('registro', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SensorPuerta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=20)),
                ('modelo', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=20)),
                ('apertura', models.BooleanField()),
                ('registro', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SensorTemperatura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=20)),
                ('modelo', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=20)),
                ('temperatura', models.FloatField()),
                ('registro', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
