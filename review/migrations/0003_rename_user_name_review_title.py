# Generated by Django 4.1 on 2022-10-28 03:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_rename_comments_review_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='user_name',
            new_name='title',
        ),
    ]
