# Generated by Django 2.1.2 on 2018-11-07 06:49

import common.models
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ansible_api', '0008_playbook_pull_policy'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeployExecution',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('timedelta', models.FloatField(default=0.0, null=True, verbose_name='Time')),
                ('state', models.CharField(choices=[('PENDING', 'Pending'), ('STARTED', 'Started'), ('SUCCESS', 'Success'), ('FAILURE', 'Failure'), ('RETRY', 'Retry')], default='PENDING', max_length=16)),
                ('num', models.IntegerField(default=1)),
                ('result_summary', common.models.JsonDictTextField(blank=True, default='{}', null=True, verbose_name='Result summary')),
                ('result_raw', common.models.JsonDictTextField(blank=True, default='{}', null=True, verbose_name='Result raw')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Create time')),
                ('date_start', models.DateTimeField(null=True, verbose_name='Start time')),
                ('date_end', models.DateTimeField(null=True, verbose_name='End time')),
            ],
            options={
                'get_latest_by': 'date_start',
            },
        ),
        migrations.CreateModel(
            name='Cluster',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('ansible_api.project',),
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('ansible_api.host',),
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('ansible_api.group',),
        ),
        migrations.AddField(
            model_name='deployexecution',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='openshift_api.Cluster'),
        ),
    ]
