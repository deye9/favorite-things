# Generated by Django 2.2.4 on 2019-08-19 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuditLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(blank=True, max_length=30)),
                ('event', models.CharField(max_length=30)),
                ('record_id', models.IntegerField(default=0)),
                ('old_values', models.TextField()),
                ('new_values', models.TextField()),
                ('url', models.URLField()),
                ('ip_address', models.GenericIPAddressField()),
                ('user_agent', models.CharField(blank=True, max_length=30, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Metadata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=30)),
                ('value', models.CharField(max_length=30)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tracker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(blank=True, max_length=300, null=True)),
                ('ranking', models.IntegerField()),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracker_category', to='backend.Category')),
                ('metadata', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tracker_metadata', to='backend.Metadata')),
            ],
        ),
    ]
