# Generated by Django 4.1.1 on 2023-07-20 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_illustration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='illustration',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
