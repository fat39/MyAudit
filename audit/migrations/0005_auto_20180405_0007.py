# Generated by Django 2.0.1 on 2018-04-04 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0004_auto_20180404_1534'),
    ]

    operations = [
        migrations.CreateModel(
            name='SessionLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='audit.Account')),
                ('host_user_bind', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='audit.HostUserBind')),
            ],
        ),
        migrations.AddField(
            model_name='auditlog',
            name='cmd',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='auditlog',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='auditlog',
            name='session',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='audit.SessionLog'),
            preserve_default=False,
        ),
    ]
