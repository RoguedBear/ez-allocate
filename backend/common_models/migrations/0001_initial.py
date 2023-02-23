# Generated by Django 4.1.6 on 2023-02-15 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('course_code', models.SlugField(max_length=10)),
                ('credits', models.SmallIntegerField()),
                ('course_type', models.CharField(choices=[('CORE', 'Core'), ('ELEC', 'Elective')], max_length=4)),
                ('programme', models.CharField(max_length=20)),
                ('original_lecture_hours', models.SmallIntegerField()),
                ('original_tutorial_hours', models.SmallIntegerField()),
                ('original_practical_hours', models.SmallIntegerField()),
                ('number_of_lecture_batches', models.SmallIntegerField()),
                ('number_of_practical_or_tutorial_batches', models.SmallIntegerField()),
                ('allotment_status', models.CharField(choices=[('NONE', 'None'), ('PART', 'Partial'), ('FULL', 'Full')], default='NONE', max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('prefferred_mode', models.CharField(choices=[('LEC', 'Lecture'), ('TUT', 'Tutorial'), ('LAB', 'Practical/Lab'), ('ANY', 'Any')], default='ANY', max_length=3)),
                ('assigned_status', models.CharField(choices=[('NONE', 'None'), ('PART', 'Partial'), ('FULL', 'Full')], default='NONE', max_length=4)),
            ],
        ),
    ]
