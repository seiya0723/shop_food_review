# Generated by Django 3.2.10 on 2022-04-27 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0003_review_ip'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='approval',
            field=models.BooleanField(default=False, verbose_name='承認済み'),
        ),
    ]
