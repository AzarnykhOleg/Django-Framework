# Generated by Django 5.1.1 on 2024-09-29 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0002_alter_client_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='phone_number',
            field=models.IntegerField(),
        ),
    ]
