# Generated by Django 2.2.12 on 2022-02-11 08:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moneyManage', '0002_fixed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='expense_date',
            field=models.DateField(default=datetime.date(2022, 2, 11)),
        ),
    ]