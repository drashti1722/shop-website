# Generated by Django 3.2.7 on 2021-11-25 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='shpping',
            name='colour',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='shpping',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
