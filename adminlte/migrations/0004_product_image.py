# Generated by Django 3.2.7 on 2021-10-08 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminlte', '0003_product_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.FileField(null=True, upload_to='products'),
        ),
    ]
