# Generated by Django 3.2.12 on 2023-12-04 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Infinitrax', '0002_brand'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=255)),
            ],
        ),
    ]