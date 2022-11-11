# Generated by Django 4.1.3 on 2022-11-11 04:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=150)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=150)),
                ('identification', models.BigIntegerField()),
                ('city', models.CharField(max_length=30)),
                ('sex', models.CharField(max_length=10)),
                ('age', models.PositiveSmallIntegerField()),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.position')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
