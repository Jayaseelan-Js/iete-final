# Generated by Django 4.0.5 on 2023-08-31 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('authors', models.CharField(max_length=255)),
                ('publication_date', models.DateField()),
                ('doi', models.CharField(max_length=255)),
                ('abstract', models.TextField()),
                ('keywords', models.CharField(max_length=255)),
            ],
        ),
    ]