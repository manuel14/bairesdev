# Generated by Django 2.1.1 on 2018-09-15 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20180915_1644'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='ratings',
            new_name='rating',
        ),
        migrations.AlterField(
            model_name='review',
            name='ip_addr',
            field=models.CharField(blank=True, max_length=39),
        ),
    ]
