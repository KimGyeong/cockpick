# Generated by Django 2.2.4 on 2019-08-09 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='null', max_length=255)),
                ('image', models.ImageField(upload_to='images/')),
                ('description', models.CharField(max_length=500)),
                ('centerx', models.CharField(default='37.3595704', max_length=255)),
                ('centery', models.CharField(default='127.105399', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Cock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='images/')),
                ('component', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
    ]
