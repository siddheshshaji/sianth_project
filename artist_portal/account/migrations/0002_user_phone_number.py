# Generated by Django 4.2.3 on 2023-07-19 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="phone_number",
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]