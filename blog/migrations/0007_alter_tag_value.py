# Generated by Django 3.2.6 on 2023-04-05 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_authorprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='value',
            field=models.TextField(max_length=100, unique=True),
        ),
    ]
