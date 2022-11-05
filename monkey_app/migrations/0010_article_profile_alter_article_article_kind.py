# Generated by Django 4.1.2 on 2022-11-04 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('monkey_app', '0009_remove_profile_name_profile_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='monkey_app.profile'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_kind',
            field=models.CharField(choices=[('Informational', 'Informational'), ('Review', 'Rewiew'), ('Not selected', 'Not selected'), ('Scinefic', 'Scientific')], default='Not selected', max_length=20),
        ),
    ]
