# Generated by Django 2.1.7 on 2019-03-15 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20190315_0417'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testimonial',
            name='picture',
        ),
        migrations.AddField(
            model_name='testimonial',
            name='picture_url',
            field=models.CharField(blank=True, max_length=400),
        ),
    ]
