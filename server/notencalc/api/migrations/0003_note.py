# Generated by Django 3.1.1 on 2020-09-08 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '0002_delete_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bezeichnung', models.CharField(max_length=100)),
                ('notenwert', models.DecimalField(decimal_places=1, max_digits=1)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
