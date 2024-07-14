# Generated by Django 5.0.7 on 2024-07-13 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido_paterno', models.CharField(max_length=50)),
                ('apellido_materno', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('nombre_cuenta', models.CharField(max_length=50, unique=True)),
                ('contrasena', models.CharField(max_length=128)),
            ],
        ),
    ]
