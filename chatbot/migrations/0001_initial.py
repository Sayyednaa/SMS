# Generated by Django 4.0.6 on 2023-03-28 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_input', models.CharField(max_length=255)),
                ('bot_response', models.TextField()),
            ],
        ),
    ]
