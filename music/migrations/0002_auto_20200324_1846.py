# Generated by Django 3.0.4 on 2020-03-24 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musician',
            name='alive',
            field=models.BooleanField(default=False),
        ),
    ]
