# Generated by Django 3.1.4 on 2023-05-06 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0008_quesmodel_det'),
    ]

    operations = [
        migrations.AddField(
            model_name='quesmodel',
            name='qid',
            field=models.IntegerField(default=0),
        ),
    ]
