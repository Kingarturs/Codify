# Generated by Django 2.2.5 on 2019-12-02 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Documentos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carpeta',
            old_name='usuario',
            new_name='username',
        ),
    ]
