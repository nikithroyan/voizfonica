# Generated by Django 4.0 on 2022-07-09 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='prepaid_recharge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_name', models.CharField(max_length=30)),
                ('benefits', models.CharField(max_length=60)),
                ('validity', models.CharField(max_length=60)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
