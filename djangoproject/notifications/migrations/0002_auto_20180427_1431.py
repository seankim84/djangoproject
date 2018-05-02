# Generated by Django 2.0.4 on 2018-04-27 05:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notifications',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='to', to=settings.AUTH_USER_MODEL),
        ),
    ]
