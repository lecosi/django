# Generated by Django 2.0.1 on 2018-10-12 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_test', '0002_auto_20181012_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
