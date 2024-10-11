# Generated by Django 4.2.13 on 2024-05-26 13:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('complete', models.BooleanField(default=False)),
            ],
        ),
    ]
