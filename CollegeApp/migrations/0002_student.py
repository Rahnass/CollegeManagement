# Generated by Django 4.0.6 on 2022-08-01 05:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CollegeApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('student_address', models.CharField(max_length=100)),
                ('student_age', models.IntegerField()),
                ('joining_date', models.DateField()),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='CollegeApp.course')),
            ],
        ),
    ]
