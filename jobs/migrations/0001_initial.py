# Generated by Django 3.2 on 2021-04-29 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available', models.BooleanField(default=True)),
                ('job_title', models.CharField(choices=[('DEV', 'Developer'), ('QA', 'Quality Analyst'), ('BA', 'Business Analyst'), ('XD', 'Experience Designer')], default='DEV', max_length=3)),
                ('job_description', models.TextField(max_length=200)),
                ('salary', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('city', models.CharField(max_length=120)),
                ('state', models.CharField(max_length=120)),
                ('company_name', models.CharField(max_length=10)),
                ('company_email', models.EmailField(max_length=254)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
