# Generated by Django 2.0.1 on 2018-01-24 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author_db',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='News_db',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('auth_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Author_db')),
            ],
        ),
    ]
