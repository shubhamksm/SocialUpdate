# Generated by Django 2.2.4 on 2019-09-18 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialupdate', '0010_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='media/ProfilePictures/'),
        ),
    ]
