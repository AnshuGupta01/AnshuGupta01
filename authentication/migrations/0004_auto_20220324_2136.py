# Generated by Django 3.0.14 on 2022-03-24 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_remark'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lead',
            name='password',
        ),
        migrations.AddField(
            model_name='lead',
            name='public',
            field=models.BooleanField(default=True),
        ),
    ]