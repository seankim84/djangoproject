# Generated by Django 2.0.4 on 2018-04-24 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20180420_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
