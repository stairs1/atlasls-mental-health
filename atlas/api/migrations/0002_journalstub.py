# Generated by Django 3.0.3 on 2020-02-23 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JournalStub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('authors_date', models.CharField(max_length=300)),
                ('relevant_questions', models.CharField(max_length=12)),
                ('summary', models.CharField(max_length=2000)),
                ('subject_group', models.CharField(max_length=2000)),
                ('other_findings', models.CharField(max_length=2000)),
                ('task_mindfullness', models.CharField(max_length=2000)),
                ('task_wellness', models.CharField(max_length=2000)),
                ('task_clinical', models.CharField(max_length=2000)),
            ],
        ),
    ]
