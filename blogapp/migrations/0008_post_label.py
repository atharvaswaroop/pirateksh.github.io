# Generated by Django 2.2.3 on 2019-07-13 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0007_auto_20190713_2010'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='label',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]