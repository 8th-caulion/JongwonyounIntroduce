# Generated by Django 3.0.5 on 2020-05-03 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('author', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('author', models.CharField(max_length=30)),
                ('pub_date', models.DateTimeField(verbose_name='data published')),
                ('modified_date', models.DateTimeField(verbose_name='data modified')),
                ('view_count', models.IntegerField()),
                ('comments', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.Comment')),
            ],
        ),
    ]
