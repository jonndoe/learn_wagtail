# Generated by Django 4.2.8 on 2023-12-15 17:24

from django.db import migrations
import modelcluster.fields


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0003_author"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogpage",
            name="authors",
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to="blog.author"),
        ),
    ]