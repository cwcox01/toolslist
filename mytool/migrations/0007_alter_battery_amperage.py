# Generated by Django 4.1.7 on 2023-04-15 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mytool', '0006_alter_battery_performance_choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='battery',
            name='amperage',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=2),
        ),
    ]