# Generated by Django 3.1.6 on 2021-02-03 17:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('credit_card', '0002_transference'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transference',
            name='transfered_from',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
