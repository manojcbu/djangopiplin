# Generated by Django 4.0.4 on 2022-05-27 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.TextField(max_length=255)),
                ('aadhaar_id', models.TextField(max_length=16)),
                ('dob', models.DateField()),
                ('state', models.TextField(max_length=255)),
                ('pin_code', models.TextField(max_length=10)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('NA', 'Prefer Not To Say')], max_length=3)),
                ('email', models.EmailField(max_length=254)),
                ('primary_phone', models.TextField(max_length=15)),
                ('other_phone', models.TextField(max_length=15)),
                ('address', models.TextField()),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('experience', models.IntegerField()),
                ('resume_status', models.CharField(choices=[('PENDING', 'In Queue'), ('SUCCESS', 'Success'), ('FAILED', 'Failed')], max_length=10)),
                ('resume_path', models.TextField()),
            ],
        ),
        migrations.AddConstraint(
            model_name='candidate',
            constraint=models.CheckConstraint(check=models.Q(('aadhaar_id__length', 16)), name='aadhaar_id_length'),
        ),
    ]
