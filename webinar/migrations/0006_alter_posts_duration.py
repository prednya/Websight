# Generated by Django 3.2.3 on 2021-06-29 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webinar', '0005_alter_posts_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='duration',
            field=models.CharField(max_length=50),
        ),
    ]
