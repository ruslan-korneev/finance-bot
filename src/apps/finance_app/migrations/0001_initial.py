# Generated by Django 3.2.6 on 2021-08-03 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('amount', models.FloatField()),
                ('date_income', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
