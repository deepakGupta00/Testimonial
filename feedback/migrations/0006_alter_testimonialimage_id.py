# Generated by Django 5.1.2 on 2024-12-31 17:35

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0005_alter_testimonial_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonialimage',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
