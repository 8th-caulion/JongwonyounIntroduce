# Generated by Django 3.0.5 on 2020-05-03 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_auto_20200503_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='comments',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainApp.Comment'),
        ),
    ]