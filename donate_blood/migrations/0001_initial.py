# Generated by Django 3.2.24 on 2024-03-12 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DonateBlood',
            fields=[
                ('blood_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('blood_group', models.CharField(max_length=45)),
                ('health_condition', models.CharField(max_length=45)),
                ('phn', models.IntegerField()),
            ],
            options={
                'db_table': 'donate_blood',
                'managed': False,
            },
        ),
    ]
