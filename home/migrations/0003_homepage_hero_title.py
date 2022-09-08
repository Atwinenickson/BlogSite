# Generated by Django 3.2.9 on 2021-11-20 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='hero_title',
            field=models.CharField(blank=True, help_text='Main text displayed in the hero section over the background.', max_length=120),
        ),
    ]
