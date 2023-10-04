# Generated by Django 4.2.4 on 2023-10-04 19:19

from django.db import migrations, models
import properties.helpers


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0005_alter_propertyimage_property'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertyimage',
            name='photos',
            field=models.ImageField(max_length=255, upload_to=properties.helpers.path_and_rename),
        ),
    ]