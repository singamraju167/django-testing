# Generated by Django 3.2.13 on 2022-07-23 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_post_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job_postings',
            name='id',
        ),
        migrations.AlterField(
            model_name='job_postings',
            name='j_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
