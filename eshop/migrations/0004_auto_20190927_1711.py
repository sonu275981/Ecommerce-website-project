# Generated by Django 2.2.5 on 2019-09-27 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0003_auto_20190927_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
