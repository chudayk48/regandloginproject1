# Generated by Django 5.0.4 on 2024-04-26 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('emailapp', '0002_delete_emailmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=10)),
                ('dob', models.DateField()),
                ('hgra', models.CharField(max_length=15)),
                ('course', models.CharField(max_length=40)),
                ('year', models.CharField(max_length=5)),
                ('mob', models.DecimalField(decimal_places=0, max_digits=10)),
                ('ename', models.EmailField(max_length=254)),
                ('pas', models.CharField(max_length=14)),
                ('cpas', models.CharField(max_length=14)),
            ],
        ),
    ]
