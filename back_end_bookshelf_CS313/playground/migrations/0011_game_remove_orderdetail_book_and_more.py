# Generated by Django 5.0.4 on 2024-05-11 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0010_rename_orderbook_orderdetail_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('about_game', models.TextField()),
                ('gameplay', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('video', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='orderdetail',
            name='book',
        ),
        migrations.RemoveField(
            model_name='orderdetail',
            name='order',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='OrderDetail',
        ),
        migrations.DeleteModel(
            name='PurchaseOrder',
        ),
    ]
