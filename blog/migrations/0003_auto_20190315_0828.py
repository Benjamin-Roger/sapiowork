# Generated by Django 2.1.7 on 2019-03-15 08:28

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190315_0750'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcategory',
            name='name_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='blogcategory',
            name='name_fr',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='blogindexpage',
            name='intro_en',
            field=wagtail.core.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blogindexpage',
            name='intro_fr',
            field=wagtail.core.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='body_en',
            field=wagtail.core.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='body_fr',
            field=wagtail.core.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='intro_en',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='intro_fr',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='blogpagegalleryimage',
            name='caption_en',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='blogpagegalleryimage',
            name='caption_fr',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
