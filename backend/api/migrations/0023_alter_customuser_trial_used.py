# Generated by Django 4.2.5 on 2024-02-22 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_customuser_company_name_customuser_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='trial_used',
            field=models.BooleanField(default=True),
        ),
    ]