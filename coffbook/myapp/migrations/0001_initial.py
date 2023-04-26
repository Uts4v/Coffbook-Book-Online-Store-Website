# Generated by Django 4.1.4 on 2023-01-03 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bought',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=120, null=True)),
                ('bookname', models.CharField(max_length=120, null=True)),
                ('price', models.CharField(max_length=120, null=0)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('name', models.CharField(max_length=120, null=True)),
                ('email', models.CharField(max_length=120, null=True)),
                ('phone', models.CharField(default='', max_length=120, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('name', models.CharField(max_length=120, null=True)),
                ('email', models.CharField(max_length=120, null=True)),
                ('phone', models.CharField(default='', max_length=120, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('username', models.CharField(max_length=120, null=True)),
                ('email', models.CharField(default='NULL', max_length=120, primary_key=True, serialize=False, unique=True)),
                ('password', models.CharField(max_length=120, null=True)),
            ],
        ),
    ]
