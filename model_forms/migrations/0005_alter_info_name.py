# Generated by Django 4.2 on 2023-06-02 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model_forms', '0004_rename_session_session2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='name',
            field=models.CharField(max_length=100, verbose_name='First name'),
        ),
    ]