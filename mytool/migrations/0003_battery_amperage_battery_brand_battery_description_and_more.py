# Generated by Django 4.1.7 on 2023-04-11 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mytool', '0002_rename_tools_battery_rename_batteries_tool'),
    ]

    operations = [
        migrations.AddField(
            model_name='battery',
            name='amperage',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='battery',
            name='brand',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='battery',
            name='description',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='battery',
            name='performance_choice',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='', max_length=1),
        ),
        migrations.AddField(
            model_name='battery',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='battery',
            name='voltage',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='tool',
            name='brand',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='tool',
            name='brushless_type',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='', max_length=1),
        ),
        migrations.AddField(
            model_name='tool',
            name='cordless_type',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='', max_length=1),
        ),
        migrations.AddField(
            model_name='tool',
            name='description',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='tool',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tool',
            name='tool_type',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='tool',
            name='voltage',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
