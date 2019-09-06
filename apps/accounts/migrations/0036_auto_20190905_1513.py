# Generated by Django 2.2.4 on 2019-09-05 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0035_auto_20190903_1959'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='password_recovery_phrase',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='organization',
            name='domain',
            field=models.CharField(blank=True, default='', help_text='A list of domains separated by white space. If populated, restrict email registration to these domains.', max_length=512, verbose_name='Email Domain(s)'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='subject',
            field=models.CharField(blank=True, db_index=True, default='153266899754651', help_text='Subject ID', max_length=64),
        ),
    ]
