# Generated by Django 3.0.5 on 2020-04-13 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='static/blog-bg.png', upload_to='images/'),
        ),
    ]
