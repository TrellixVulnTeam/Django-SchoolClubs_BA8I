# Generated by Django 3.1.4 on 2021-01-18 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0020_auto_20210118_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='club_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
