# Generated by Django 4.1.1 on 2022-09-15 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
    ]
