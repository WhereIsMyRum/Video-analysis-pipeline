# Generated by Django 2.2.5 on 2019-10-22 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstorageentries',
            name='analyzed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userstorageentries',
            name='clips_no',
            field=models.IntegerField(default=0),
        ),
    ]