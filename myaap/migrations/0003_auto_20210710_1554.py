# Generated by Django 3.1.6 on 2021-07-10 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myaap', '0002_search_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='category',
            field=models.CharField(default='sss', max_length=20, null=True),
        ),
    ]