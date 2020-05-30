# Generated by Django 2.2.5 on 2020-05-30 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('date', models.DateField(auto_now_add=True)),
                ('Name', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('Desc', models.TextField()),
                ('Price', models.IntegerField()),
                ('Choice', models.CharField(choices=[('1', 'Gaming'), ('2', 'Workstation'), ('3', 'Domestic')], max_length=1)),
                ('Image1', models.ImageField(default='uploads/image-available.jpg', upload_to='uploads/')),
                ('Image2', models.ImageField(default='uploads/image-available.jpg', upload_to='uploads/')),
                ('Image3', models.ImageField(default='uploads/image-available.jpg', upload_to='uploads/')),
                ('Image4', models.ImageField(default='uploads/image-available.jpg', upload_to='uploads/')),
                ('Image5', models.ImageField(default='uploads/image-available.jpg', upload_to='uploads/')),
                ('CPU', models.CharField(choices=[('1', 'Intel'), ('2', 'AMD')], max_length=1)),
                ('CPU_MODEL', models.CharField(max_length=100)),
                ('RAM', models.CharField(choices=[('1', 'DDR3'), ('2', 'DDR4')], max_length=1)),
                ('RAM_SPEED', models.CharField(max_length=100)),
                ('GPU', models.CharField(choices=[('1', 'Nvidia'), ('2', 'AMD')], max_length=2)),
                ('GPU_Model', models.CharField(max_length=100)),
                ('SSD', models.BooleanField(blank=True, null=True)),
                ('SSD_BRAND', models.CharField(max_length=100)),
                ('HDD', models.CharField(choices=[('1', '2 TB'), ('2', '1 TB')], max_length=1)),
                ('HDD_BRAND', models.CharField(max_length=100)),
                ('RefreshRate', models.CharField(max_length=10)),
                ('OS', models.CharField(max_length=100)),
                ('WARRANTY', models.CharField(max_length=100)),
                ('Dealer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Desktop',
            fields=[
                ('date', models.DateField(auto_now_add=True)),
                ('Name', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('Desc', models.TextField()),
                ('Price', models.IntegerField()),
                ('Choice', models.CharField(choices=[('1', 'Gaming'), ('2', 'Workstation'), ('3', 'Domestic')], max_length=1)),
                ('Image1', models.ImageField(default='uploads/image-available.jpg', upload_to='uploads/')),
                ('Image2', models.ImageField(default='uploads/image-available.jpg', upload_to='uploads/')),
                ('Image3', models.ImageField(default='uploads/image-available.jpg', upload_to='uploads/')),
                ('Image4', models.ImageField(default='uploads/image-available.jpg', upload_to='uploads/')),
                ('Image5', models.ImageField(default='uploads/image-available.jpg', upload_to='uploads/')),
                ('CPU', models.CharField(choices=[('1', 'Intel'), ('2', 'AMD')], max_length=1)),
                ('CPU_MODEL', models.CharField(max_length=100)),
                ('RAM', models.CharField(choices=[('1', 'DDR3'), ('2', 'DDR4')], max_length=1)),
                ('RAM_SPEED', models.CharField(max_length=100)),
                ('GPU', models.CharField(choices=[('1', 'Nvidia'), ('2', 'AMD')], max_length=2)),
                ('GPU_Model', models.CharField(max_length=100)),
                ('SSD', models.BooleanField(blank=True, null=True)),
                ('SSD_BRAND', models.CharField(blank=True, max_length=100, null=True)),
                ('HDD', models.CharField(choices=[('1', '2 TB'), ('2', '1 TB')], max_length=1)),
                ('HDD_BRAND', models.CharField(max_length=100)),
                ('RefreshRate', models.CharField(max_length=10)),
                ('OS', models.CharField(max_length=100)),
                ('WARRANTY', models.CharField(max_length=100)),
                ('Dealer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Comment', models.CharField(max_length=150)),
                ('Product', models.CharField(max_length=150)),
                ('Date', models.DateTimeField(auto_now_add=True)),
                ('Upvotes', models.IntegerField()),
                ('Downvotes', models.IntegerField()),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Accounts.Profile')),
            ],
        ),
    ]