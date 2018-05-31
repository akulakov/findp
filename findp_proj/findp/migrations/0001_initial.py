# Generated by Django 2.0.5 on 2018-05-30 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RecordP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True)),
                ('forum', models.CharField(max_length=300)),
                ('site', models.CharField(choices=[('Reddit', 'Reddit')], max_length=200)),
                ('num_p', models.IntegerField()),
            ],
        ),
    ]