# Generated by Django 3.2.9 on 2022-04-08 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registeration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=69)),
                ('Address', models.CharField(max_length=120)),
                ('Email', models.EmailField(max_length=254)),
                ('Mobile', models.CharField(max_length=13)),
                ('Password', models.CharField(max_length=69)),
                ('Gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Male', max_length=10)),
            ],
        ),
    ]