# Generated by Django 2.2 on 2021-11-10 02:29

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, verbose_name='First name')),
                ('last_name', models.CharField(max_length=20, verbose_name='Last name')),
                ('address', models.CharField(max_length=50, verbose_name='Address')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Phone')),
                ('identity_type', models.CharField(choices=[('DNI', 'DNI'), ('PASSPORT', 'PASSPORT'), ('RESIDENCE', 'RESIDENCE')], max_length=10, verbose_name='Identity_type')),
                ('identity', models.CharField(max_length=30, unique=True, verbose_name='Identity')),
                ('email', models.CharField(max_length=25, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customers',
            },
        ),
    ]
