# Generated by Django 3.0.5 on 2020-04-29 13:29

from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0007_auto_20200429_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='image',
            field=sorl.thumbnail.fields.ImageField(upload_to='portfolio'),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='image',
            field=models.ImageField(upload_to='testimonial'),
        ),
    ]
