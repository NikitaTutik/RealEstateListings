# Generated by Django 4.2.4 on 2023-10-02 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0004_alter_propertyimage_property'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertyimage',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='properties.property'),
        ),
    ]