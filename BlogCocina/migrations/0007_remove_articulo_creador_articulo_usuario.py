# Generated by Django 4.2.1 on 2023-05-27 22:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('BlogCocina', '0006_articulo_fecha'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articulo',
            name='creador',
        ),
        migrations.AddField(
            model_name='articulo',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
