# Generated by Django 3.0.5 on 2020-05-23 08:06
from django.db import migrations, models
class Migration(migrations.Migration):
    dependencies = [
        ('hospital', '0011_auto_20200523_1325'),
    ]
    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pic/DoctorProfilePic/'),
        ),
    ]