# Generated by Django 4.2.5 on 2023-09-24 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admn', '0018_alter_books_borow_dt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='borow_dt',
            field=models.TextField(null=True),
        ),
    ]
