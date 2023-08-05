# Generated by Django 4.1.5 on 2023-08-05 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dailypulse', '0005_rename_news_id_comment_news_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.TextField(blank=True, default='', null=True)),
                ('author', models.TextField(blank=True, default='', null=True)),
                ('title', models.TextField(blank=True, default='', null=True)),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('url', models.URLField(blank=True, default='', null=True)),
                ('url_image', models.URLField(blank=True, default='', null=True)),
                ('published_date', models.DateField(default='1996-07-30')),
                ('content', models.TextField(blank=True, default='', null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='news',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dailypulse.news'),
        ),
        migrations.DeleteModel(
            name='New',
        ),
    ]
