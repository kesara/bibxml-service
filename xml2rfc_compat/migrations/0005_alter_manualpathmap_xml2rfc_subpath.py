# Generated by Django 4.0.2 on 2022-02-09 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xml2rfc_compat', '0004_remove_manualpathmap_query_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manualpathmap',
            name='xml2rfc_subpath',
            field=models.CharField(db_index=True, max_length=255, unique=True),
        ),
    ]
