# Generated by Django 4.2.13 on 2024-08-06 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_delete_backgroundmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='SkillModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('level', models.PositiveBigIntegerField(default=50)),
            ],
        ),
    ]
