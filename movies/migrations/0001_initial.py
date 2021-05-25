# Generated by Django 3.2.3 on 2021-05-25 04:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('owners', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('age', models.IntegerField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='owners.owner')),
            ],
            options={
                'db_table': 'movies',
            },
        ),
    ]
