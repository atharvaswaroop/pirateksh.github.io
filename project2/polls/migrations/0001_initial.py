# Generated by Django 2.1.5 on 2019-02-07 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ques_no', models.IntegerField(verbose_name='Question Number')),
                ('ques_text', models.CharField(max_length=1000, verbose_name='Text')),
                ('pub_date', models.DateField(verbose_name='Publication Date')),
            ],
        ),
    ]