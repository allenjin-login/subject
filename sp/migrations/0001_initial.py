# Generated by Django 3.2 on 2021-05-04 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=50)),
                ('add_time', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
