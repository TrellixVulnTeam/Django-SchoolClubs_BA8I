# Generated by Django 3.1.4 on 2021-01-14 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0011_announcement_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='club',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='clubs.club'),
        ),
    ]
