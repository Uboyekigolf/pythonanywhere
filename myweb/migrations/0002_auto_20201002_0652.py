# Generated by Django 2.2.7 on 2020-10-02 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myweb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='herb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('herb_type', models.CharField(max_length=200)),
                ('herb_name', models.CharField(max_length=200)),
                ('herb_properties', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='herbtype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('herbtype_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]