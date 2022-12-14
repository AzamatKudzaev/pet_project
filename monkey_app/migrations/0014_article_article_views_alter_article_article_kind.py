# Generated by Django 4.1.2 on 2022-11-05 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monkey_app', '0013_alter_article_article_kind_alter_article_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_views',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_kind',
            field=models.CharField(choices=[('Scinefic', 'Scientific'), ('Informational', 'Informational'), ('Review', 'Rewiew'), ('Not selected', 'Not selected')], default='Not selected', max_length=20),
        ),
    ]
