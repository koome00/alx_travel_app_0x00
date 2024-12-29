# Generated by Django 5.1.4 on 2024-12-29 18:39

import alx_travel_app.listings.models
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('review_id', models.UUIDField(default=alx_travel_app.listings.models.generate_uuid, primary_key=True, serialize=False)),
                ('comment', models.TextField()),
                ('rating', models.IntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('property_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to='listings.property')),
            ],
        ),
    ]
