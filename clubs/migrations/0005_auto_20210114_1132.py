# Generated by Django 3.1.4 on 2021-01-14 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0004_auto_20210114_1115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advisor',
            name='userId',
        ),
        migrations.RemoveField(
            model_name='student',
            name='userId',
        ),
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('until_date', models.DateTimeField(blank=True, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('event_name', models.CharField(blank=True, max_length=150, null=True)),
                ('location', models.CharField(blank=True, max_length=150, null=True)),
                ('club', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='clubs.club')),
                ('publisher', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clubs.student')),
            ],
        ),
    ]
