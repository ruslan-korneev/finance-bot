# Generated by Django 3.2.6 on 2021-08-05 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance_app', '0005_liability_nameliability'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='asset',
            options={'verbose_name': 'Asset', 'verbose_name_plural': 'Assets'},
        ),
        migrations.AlterModelOptions(
            name='expense',
            options={'verbose_name': 'Expense', 'verbose_name_plural': 'Expenses'},
        ),
        migrations.AlterModelOptions(
            name='income',
            options={'verbose_name': 'Income', 'verbose_name_plural': 'Incomes'},
        ),
        migrations.AlterModelOptions(
            name='liability',
            options={'verbose_name': 'Liability', 'verbose_name_plural': 'Liabilities'},
        ),
        migrations.AlterModelOptions(
            name='nameasset',
            options={'verbose_name': 'Name Asset', 'verbose_name_plural': 'Names Assets'},
        ),
        migrations.AlterModelOptions(
            name='nameexpense',
            options={'verbose_name': 'Name Expense', 'verbose_name_plural': 'Names Expenses'},
        ),
        migrations.AlterModelOptions(
            name='nameincome',
            options={'verbose_name': 'Name Income', 'verbose_name_plural': 'Names Incomes'},
        ),
        migrations.AlterModelOptions(
            name='nameliability',
            options={'verbose_name': 'Name Liability', 'verbose_name_plural': 'Names Liabilities'},
        ),
        migrations.AlterModelTable(
            name='asset',
            table='assets',
        ),
        migrations.AlterModelTable(
            name='expense',
            table='expenses',
        ),
        migrations.AlterModelTable(
            name='income',
            table='incomes',
        ),
        migrations.AlterModelTable(
            name='liability',
            table='liabilities',
        ),
    ]
