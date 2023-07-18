# Generated by Django 3.2.20 on 2023-07-18 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_profile_nickname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='is_delete',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='is_delete',
        ),
        migrations.AlterField(
            model_name='profile',
            name='nickname',
            field=models.CharField(default='<django.db.models.query_utils.DeferredAttribute object at 0x000002486946EF88><django.db.models.query_utils.DeferredAttribute object at 0x000002486946EF08>', max_length=16, unique=True),
        ),
    ]