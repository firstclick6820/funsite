# Generated by Django 4.1.2 on 2022-10-12 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_alter_userbasicinfo_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbasicinfo',
            name='gender',
            field=models.TextField(default='MALE', verbose_name={('MALE', 'M'), ('FEMALE', 'F')}),
        ),
    ]
