# Generated by Django 3.1.1 on 2020-09-15 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='notenwert',
            field=models.DecimalField(decimal_places=2, max_digits=2),
        ),
    ]
