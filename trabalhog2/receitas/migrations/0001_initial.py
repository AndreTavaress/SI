# Generated by Django 5.0.1 on 2024-11-18 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='receita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredientes', models.CharField(max_length=1000)),
                ('receita_criada', models.CharField(max_length=10000)),
            ],
        ),
    ]
