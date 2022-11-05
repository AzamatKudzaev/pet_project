# Generated by Django 4.1.2 on 2022-11-04 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('monkey_app', '0010_article_profile_alter_article_article_kind'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_kind',
            field=models.CharField(choices=[('Not selected', 'Not selected'), ('Review', 'Rewiew'), ('Scinefic', 'Scientific'), ('Informational', 'Informational')], default='Not selected', max_length=20),
        ),
        migrations.AlterField(
            model_name='article',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='monkey_app.profile'),
        ),
    ]