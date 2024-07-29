# Generated by Django 5.0.6 on 2024-05-20 12:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_alter_article_pub_date_alter_article_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2024, 5, 20, 12, 6, 55, 161073, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, default=1, unique=True),
            preserve_default=False,
        ),
    ]
