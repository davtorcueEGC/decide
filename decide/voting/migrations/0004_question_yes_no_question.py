# Generated by Django 2.0 on 2021-01-04 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0003_auto_20180605_0842'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='yes_no_question',
            field=models.BooleanField(default=False, help_text='Check the box to generate automatically the options yes/no ', verbose_name='Yes/No question'),
        ),
    ]
