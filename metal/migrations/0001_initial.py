# Generated by Django 3.2.18 on 2023-04-14 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RequestCallBack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.TextField()),
                ('user_mail', models.TextField()),
                ('user_number', models.TextField()),
                ('user_element', models.TextField()),
                ('user_message', models.TextField()),
            ],
        ),
    ]
