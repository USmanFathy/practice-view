# Generated by Django 4.1.1 on 2022-09-26 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0003_tool_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tool',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
