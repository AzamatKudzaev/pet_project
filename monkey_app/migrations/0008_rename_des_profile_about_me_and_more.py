# Generated by Django 4.1.2 on 2022-11-04 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monkey_app', '0007_rename_description_profile_des_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='des',
            new_name='about_me',
        ),
        migrations.AlterField(
            model_name='article',
            name='article_kind',
            field=models.CharField(choices=[('Informational', 'Informational'), ('Review', 'Rewiew'), ('Not selected', 'Not selected'), ('Scinefic', 'Scientific')], default='Not selected', max_length=20),
        ),
    ]