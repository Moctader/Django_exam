# Generated by Django 4.2.3 on 2023-08-12 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='to_do_model',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]