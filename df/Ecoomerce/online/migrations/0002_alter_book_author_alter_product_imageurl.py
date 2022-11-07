# Generated by Django 4.0.5 on 2022-06-09 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='imageUrl',
            field=models.URLField(null=True),
        ),
    ]
