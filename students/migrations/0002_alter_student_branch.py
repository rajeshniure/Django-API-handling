# Generated by Django 5.2.1 on 2025-05-24 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='branch',
            field=models.CharField(max_length=50),
        ),
    ]
