# Generated by Django 4.1 on 2023-01-22 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='topsis_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataset', models.FileField(upload_to='topsis_data_store/')),
                ('weights', models.CharField(max_length=1000)),
                ('impacts', models.CharField(max_length=1000)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
