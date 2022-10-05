# Generated by Django 4.0.1 on 2022-10-05 08:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('username', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=150)),
                ('Seller', models.BooleanField(blank=True, null=True)),
                ('Address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Class', models.CharField(choices=[('1', 'Desktop'), ('2', 'Laptop')], max_length=1)),
                ('SubClass', models.CharField(choices=[('1', 'Gaming'), ('2', 'Workstation'), ('3', 'Domestic')], max_length=1)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
