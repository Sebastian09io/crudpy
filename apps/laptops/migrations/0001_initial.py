# Generated by Django 5.0.4 on 2024-04-09 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='laptop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('procesador', models.CharField(max_length=100)),
                ('generacion', models.IntegerField()),
                ('sistema', models.CharField(max_length=100)),
                ('ram', models.CharField(max_length=100)),
                ('rom', models.CharField(max_length=100)),
            ],
        ),
    ]