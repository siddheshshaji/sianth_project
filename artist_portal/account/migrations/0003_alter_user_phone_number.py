# Generated by Django 4.2.3 on 2023-07-19 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0002_user_phone_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="phone_number",
            field=models.CharField(max_length=255),
        ),
    ]
