# Generated by Django 4.1 on 2022-09-02 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_job_display_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='languages',
            field=models.CharField(default='Text', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='short_description',
            field=models.CharField(default='Text', max_length=500),
            preserve_default=False,
        ),
    ]
