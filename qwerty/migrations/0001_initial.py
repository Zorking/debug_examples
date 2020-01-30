# Generated by Django 3.0.2 on 2020-01-29 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Films',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nconst', models.CharField(blank=True, max_length=3000)),
                ('primaryName', models.CharField(blank=True, max_length=3000)),
                ('birthYear', models.CharField(blank=True, max_length=3000)),
                ('deathYear', models.CharField(blank=True, max_length=3000)),
                ('primaryProfession', models.CharField(blank=True, max_length=3000)),
                ('knownForTitles', models.CharField(blank=True, max_length=3000)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('cost', models.CharField(max_length=255)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qwerty.Customer')),
            ],
        ),
    ]
