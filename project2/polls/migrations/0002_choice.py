# Generated by Django 2.1.5 on 2019-02-07 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_no', models.IntegerField(verbose_name='Choice Number')),
                ('choice_text', models.CharField(max_length=500, verbose_name='Text')),
                ('no_of_votes', models.IntegerField(verbose_name='Number of Votes')),
            ],
        ),
    ]
