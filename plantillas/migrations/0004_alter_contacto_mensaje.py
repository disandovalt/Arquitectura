# Generated by Django 5.0.6 on 2024-06-26 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plantillas', '0003_contacto_mensaje'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='mensaje',
            field=models.TextField(),
        ),
    ]