# Generated by Django 2.0.1 on 2018-03-16 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apptest', '0004_auto_20180313_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tfirstpageproduct',
            name='fk_product',
            field=models.IntegerField(blank=True, db_column='Fk_Product', null=True),
        ),
    ]
