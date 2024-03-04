# Generated by Django 5.0.2 on 2024-02-29 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=250)),
                ('price', models.IntegerField()),
                ('release_date', models.CharField(max_length=50)),
                ('lte_exists', models.BooleanField()),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
    ]
