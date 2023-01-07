# Generated by Django 4.0.5 on 2022-12-29 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(blank=True, max_length=20, null=True, verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='firstname',
            field=models.CharField(max_length=100, null=True, verbose_name='Fisrt name'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='lastname',
            field=models.CharField(max_length=100, null=True, verbose_name='Last name'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Phone'),
        ),
    ]