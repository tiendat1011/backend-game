# Generated by Django 4.2 on 2024-05-12 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0014_alter_gamedetail_date_released'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameinfo',
            name='gameplay',
            field=models.TextField(null=True),
        ),
    ]
