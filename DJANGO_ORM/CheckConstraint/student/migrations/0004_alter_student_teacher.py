# Generated by Django 5.1.2 on 2024-10-17 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_alter_student_teacher_student_age10_20'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='teacher',
            field=models.CharField(max_length=100),
        ),
    ]
