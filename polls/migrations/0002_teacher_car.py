# Generated by Django 4.2.5 on 2023-09-26 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='car',
            field=models.CharField(default='bicycle', max_length=80),
            preserve_default=False,
        ),
    ]
