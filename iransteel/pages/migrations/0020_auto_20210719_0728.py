# Generated by Django 3.2.5 on 2021-07-19 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0019_auto_20210719_0722'),
    ]

    operations = [
        migrations.CreateModel(
            name='Headerparam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('param', models.CharField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Headertitel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Header',
        ),
    ]
