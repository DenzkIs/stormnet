# Generated by Django 4.2 on 2023-05-21 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model_forms', '0002_alter_info_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_id', models.CharField(max_length=100)),
                ('count', models.IntegerField()),
                ('time_create', models.TimeField(auto_now=True)),
            ],
        ),
    ]
