# Generated by Django 3.1.2 on 2021-08-15 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20210815_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brends',
            field=models.IntegerField(choices=[('1 brend', '1 brend'), ('2 brend', '2 brend'), ('3 brend', '3 brend')], max_length=200, null=True),
        ),
    ]
