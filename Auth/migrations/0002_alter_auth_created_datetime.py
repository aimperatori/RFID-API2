# Generated by Django 3.2.4 on 2021-06-26 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auth',
            name='created_DateTime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]