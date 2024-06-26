# Generated by Django 5.0.4 on 2024-05-06 16:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyurtma',
            fields=[
                ('raqam', models.AutoField(primary_key=True, serialize=False)),
                ('sana', models.DateTimeField(auto_now_add=True)),
                ('hisoblandi', models.PositiveIntegerField(default=0)),
                ('joy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.joy')),
            ],
            options={
                'verbose_name': 'Buyurtma',
                'verbose_name_plural': 'Buyurtmalar',
            },
        ),
        migrations.CreateModel(
            name='BuyurtmaIchimlik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soni', models.PositiveIntegerField(default=1)),
                ('buyurtma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='statsApp.buyurtma')),
                ('ichimlik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.ichimlik')),
            ],
            options={
                'verbose_name': 'Ichimlik',
                'verbose_name_plural': 'Ichimliklar',
            },
        ),
        migrations.CreateModel(
            name='BuyurtmaTaom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soni', models.PositiveIntegerField(default=1)),
                ('buyurtma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='statsApp.buyurtma')),
                ('taom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.taom')),
            ],
            options={
                'verbose_name': 'Taom',
                'verbose_name_plural': 'Taomlar',
            },
        ),
    ]
