# Generated by Django 5.0.6 on 2024-06-09 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Human',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Human name')),
                ('age', models.PositiveIntegerField(verbose_name='Human age')),
            ],
        ),
    ]
