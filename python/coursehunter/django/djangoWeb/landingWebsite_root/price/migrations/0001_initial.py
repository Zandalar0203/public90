# Generated by Django 4.0.4 on 2022-06-23 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PriceCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pc_value', models.CharField(max_length=20, verbose_name='Ціна')),
                ('pc_description', models.CharField(max_length=200, verbose_name='Опис')),
            ],
        ),
        migrations.CreateModel(
            name='PriceTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pt_title', models.CharField(max_length=200, verbose_name='Послуга')),
                ('pt_old_price', models.CharField(max_length=20, verbose_name='Стара ціна')),
                ('pt_new_price', models.CharField(max_length=20, verbose_name='Нова ціна')),
            ],
        ),
    ]