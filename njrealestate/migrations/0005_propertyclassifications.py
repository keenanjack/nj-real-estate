# Generated by Django 3.0.3 on 2020-02-29 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('njrealestate', '0004_auto_20200229_1514'),
    ]

    operations = [
        migrations.CreateModel(
            name='Propertyclassifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=3)),
                ('category', models.CharField(max_length=60)),
            ],
        ),
    ]
