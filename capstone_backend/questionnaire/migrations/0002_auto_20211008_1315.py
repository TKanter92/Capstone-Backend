# Generated by Django 3.2.8 on 2021-10-08 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionnaire',
            name='carpeting',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='patterns',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='rugs',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='textures',
            field=models.BooleanField(default=False),
        ),
    ]
