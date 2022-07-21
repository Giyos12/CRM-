# Generated by Django 4.0.6 on 2022-07-20 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_course_channel_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='account',
        ),
        migrations.AddField(
            model_name='account',
            name='price',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='account', to='crm.payment'),
            preserve_default=False,
        ),
    ]
