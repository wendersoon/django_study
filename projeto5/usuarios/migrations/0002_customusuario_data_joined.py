# Generated by Django 4.2.6 on 2023-10-31 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customusuario',
            name='data_joined',
            field=models.DateTimeField(auto_now_add=True, default='UTC'),
            preserve_default=False,
        ),
    ]
