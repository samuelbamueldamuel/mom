# Generated by Django 4.2.4 on 2024-01-03 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='chosen',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='task',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
