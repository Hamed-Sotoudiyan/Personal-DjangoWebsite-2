# Generated by Django 4.1.1 on 2022-09-26 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='abstract',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='articles',
            name='publisher',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='articles',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
