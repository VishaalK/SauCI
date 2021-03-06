# Generated by Django 2.1.7 on 2019-04-09 06:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Build',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('completed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField()),
                ('completed_at', models.DateTimeField()),
            ],
        ),
    ]
