# Generated by Django 4.0.3 on 2022-03-29 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='category',
            field=models.CharField(choices=[('JANUARY', 'JANUARY'), ('FEBRUARY', 'FEBRUARY'), ('MAR', 'MAR')], default='JANUARY', max_length=9),
        ),
    ]
