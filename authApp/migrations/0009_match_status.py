# Generated by Django 5.2 on 2025-04-30 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0008_session'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='pending', max_length=20),
        ),
    ]
