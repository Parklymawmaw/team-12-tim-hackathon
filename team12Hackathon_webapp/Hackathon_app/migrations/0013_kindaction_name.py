# Generated by Django 3.0.8 on 2020-07-03 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hackathon_app', '0012_auto_20200703_2153'),
    ]

    operations = [
        migrations.AddField(
            model_name='kindaction',
            name='Name',
            field=models.CharField(default='Azione Generica', max_length=2000),
            preserve_default=False,
        ),
    ]
