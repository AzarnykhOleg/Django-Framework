# Generated by Django 5.1.1 on 2024-10-12 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0004_alter_client_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_ordered',
            field=models.DateTimeField(),
        ),
    ]