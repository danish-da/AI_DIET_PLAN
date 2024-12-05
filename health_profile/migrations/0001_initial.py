# Generated by Django 3.2.24 on 2024-03-12 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HealthProfile',
            fields=[
                ('health_id', models.AutoField(primary_key=True, serialize=False)),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('body_type', models.CharField(max_length=45)),
                ('working_hour', models.TimeField()),
            ],
            options={
                'db_table': 'health_profile',
                'managed': False,
            },
        ),
    ]
