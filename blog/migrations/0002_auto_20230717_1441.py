# Generated by Django 3.2.20 on 2023-07-17 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='status',
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]