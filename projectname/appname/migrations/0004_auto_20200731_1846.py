# Generated by Django 3.0.8 on 2020-07-31 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appname', '0003_auto_20200728_1936'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='hashtag_field',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='post',
            name='hashtags',
            field=models.ManyToManyField(blank=True, to='appname.Hashtag'),
        ),
    ]