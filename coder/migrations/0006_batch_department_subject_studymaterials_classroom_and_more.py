# Generated by Django 4.1.3 on 2022-11-23 09:22

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('coder', '0005_alter_staffuser_joined_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('end_date', models.DateField(default=django.utils.timezone.now)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(default='', max_length=100)),
                ('short_name', models.CharField(blank=True, default='', max_length=20)),
                ('hod', models.CharField(default='', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('batch', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='coder.batch')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('regulation', models.DateField(default=django.utils.timezone.now)),
                ('subject_name', models.CharField(default='', max_length=100)),
                ('subject_code', models.CharField(default='', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('upated_at', models.DateTimeField(auto_now=True)),
                ('department', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='coder.department')),
            ],
        ),
        migrations.CreateModel(
            name='StudyMaterials',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('material_title', models.CharField(default='', max_length=200)),
                ('material', models.URLField(default='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('upated_at', models.DateTimeField(auto_now=True)),
                ('subject', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='coder.subject')),
            ],
        ),
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('count', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('upated_at', models.DateTimeField(auto_now=True)),
                ('batch', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='coder.batch')),
                ('department', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='coder.department')),
            ],
        ),
        migrations.AlterField(
            model_name='staffuser',
            name='department',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='coder.department'),
        ),
        migrations.AlterField(
            model_name='studentuser',
            name='department',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='coder.department'),
        ),
    ]