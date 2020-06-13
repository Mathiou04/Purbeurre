# Generated by Django 3.0.3 on 2020-06-12 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('purbeurre', '0002_auto_20200610_1355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='search',
            name='substitute',
        ),
        migrations.AlterField(
            model_name='search',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purbeurre.Product'),
        ),
    ]