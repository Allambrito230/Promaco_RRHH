# Generated by Django 5.0.11 on 2025-02-07 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permisos', '0013_alter_jefes_correo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jefes',
            name='identidadjefe',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
