# Generated by Django 2.2 on 2019-04-20 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20190419_1156'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='email',
            field=models.EmailField(default=False, max_length=254),
        ),
    ]
