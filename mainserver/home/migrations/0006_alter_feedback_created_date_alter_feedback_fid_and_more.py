# Generated by Django 5.1.1 on 2024-10-17 19:40

import datetime
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_feedback_created_date_alter_feedback_fid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='created_date',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2024, 10, 18, 1, 10, 52, 831596)),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='fid',
            field=models.UUIDField(default=uuid.UUID('7db1643a-8c5d-4b99-b6f3-53799b302264'), editable=False, unique=True),
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='user',
        ),
        migrations.AddField(
            model_name='feedback',
            name='user',
            field=models.ManyToManyField(related_name='feedbackuser', to=settings.AUTH_USER_MODEL),
        ),
    ]