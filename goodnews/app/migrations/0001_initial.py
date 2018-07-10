# Generated by Django 2.0.6 on 2018-06-29 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Verse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=100)),
                ('book_abbr', models.CharField(max_length=10)),
                ('chapter_number', models.IntegerField()),
                ('verse_number', models.IntegerField()),
                ('verse_text', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='tag',
            name='verse',
            field=models.ManyToManyField(to='app.Verse'),
        ),
    ]
