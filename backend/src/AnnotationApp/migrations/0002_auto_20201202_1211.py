# Generated by Django 3.1.3 on 2020-12-02 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AnnotationApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labels',
            name='Color',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='labels',
            name='Description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='labels',
            name='LabelName',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
