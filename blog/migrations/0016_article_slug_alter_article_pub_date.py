# Generated by Django 5.0.6 on 2024-05-20 11:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_alter_article_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2024, 5, 20, 11, 48, 34, 742059, tzinfo=datetime.timezone.utc)),
        ),
    ]
