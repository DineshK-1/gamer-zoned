# Generated by Django 2.2.5 on 2020-05-30 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DB', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='Date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]