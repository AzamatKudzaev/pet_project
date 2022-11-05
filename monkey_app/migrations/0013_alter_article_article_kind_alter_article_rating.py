# Generated by Django 4.1.2 on 2022-11-05 05:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monkey_app', '0012_profile_sex_alter_article_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_kind',
            field=models.CharField(choices=[('Informational', 'Informational'), ('Not selected', 'Not selected'), ('Scinefic', 'Scientific'), ('Review', 'Rewiew')], default='Not selected', max_length=20),
        ),
        migrations.AlterField(
            model_name='article',
            name='rating',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]