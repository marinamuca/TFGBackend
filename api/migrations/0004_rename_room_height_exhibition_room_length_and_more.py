# Generated by Django 4.1.1 on 2023-07-30 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_illustration_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exhibition',
            old_name='room_height',
            new_name='room_length',
        ),
        migrations.AddField(
            model_name='illustration',
            name='position',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='illustration',
            name='image',
            field=models.ImageField(default='illustrations/default-placeholder.png', upload_to='illustrations'),
        ),
    ]
