# Generated by Django 4.2.7 on 2023-11-27 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_article', models.CharField(max_length=20)),
                ('numero_articles', models.IntegerField()),
                ('Create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]