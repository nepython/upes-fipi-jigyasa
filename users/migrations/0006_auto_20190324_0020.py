# Generated by Django 2.1.7 on 2019-03-23 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20190312_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_details',
            name='referral',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='REFERRAL'),
        ),
        migrations.AlterField(
            model_name='user_details',
            name='status',
            field=models.CharField(default='Not Paid', max_length=12, verbose_name='STATUS'),
        ),
    ]
