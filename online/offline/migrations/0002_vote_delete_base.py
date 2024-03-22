# Generated by Django 5.0.1 on 2024-03-13 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offline', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote_id', models.BigIntegerField()),
                ('age', models.IntegerField()),
                ('birth', models.DateField()),
                ('mandal', models.CharField(max_length=50)),
                ('distic', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='base',
        ),
    ]
