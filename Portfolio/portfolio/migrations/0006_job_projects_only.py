# Generated by Django 4.1 on 2022-09-02 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_alter_project_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='projects_only',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
