# Generated by Django 4.1.2 on 2022-11-05 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monkey_app', '0015_article_article_dislike_article_article_like_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='article_dislike',
        ),
        migrations.RemoveField(
            model_name='article',
            name='article_like',
        ),
        migrations.AddField(
            model_name='article',
            name='article_dislikes',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='article_likes',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_kind',
            field=models.CharField(choices=[('Review', 'Rewiew'), ('Not selected', 'Not selected'), ('Informational', 'Informational'), ('Scinefic', 'Scientific')], default='Not selected', max_length=20),
        ),
    ]
