# Generated by Django 4.1.1 on 2023-08-17 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_rename_room_height_exhibition_room_length_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='illustration',
            options={'ordering': ['position', 'id']},
        ),
        migrations.AlterField(
            model_name='illustration',
            name='image',
            field=models.ImageField(upload_to='illustrations'),
        ),
    ]
