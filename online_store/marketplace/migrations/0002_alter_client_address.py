# Generated by Django 5.1.1 on 2024-09-28 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='address',
            field=models.TextField(),
        ),
    ]