# Generated by Django 2.2.3 on 2020-06-30 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='age',
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='asdfasdf', max_length=255),
            preserve_default=False,
        ),
    ]
