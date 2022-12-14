# Generated by Django 4.1.2 on 2022-11-04 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monkey_app', '0008_rename_des_profile_about_me_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_kind',
            field=models.CharField(choices=[('Scinefic', 'Scientific'), ('Review', 'Rewiew'), ('Not selected', 'Not selected'), ('Informational', 'Informational')], default='Not selected', max_length=20),
        ),
    ]
