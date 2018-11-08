# Generated by Django 2.0 on 2018-11-08 02:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0002_event_creator'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_registered', models.DateTimeField(auto_now_add=True, verbose_name='Date Registered')),
                ('parents_permit', models.FileField(default='', upload_to='uploads/', verbose_name="Parent's Permit")),
                ('waiver', models.FileField(default='', upload_to='uploads/', verbose_name='Waiver')),
                ('parents_contact_number', models.CharField(max_length=50, verbose_name="Parent's Contact Number")),
                ('status', models.CharField(default='Approved', max_length=11, verbose_name='Status')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
