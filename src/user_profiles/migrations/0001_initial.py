# Generated by Django 5.1.5 on 2025-03-02 14:45

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, validators=[django.core.validators.MaxLengthValidator(1000, message='Максимальная длина биографии 1000 символов.')])),
                ('university_group', models.CharField(blank=True, max_length=16, null=True)),
                ('codeforces_handle', models.CharField(max_length=24)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
