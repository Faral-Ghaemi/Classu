# Generated by Django 2.1.7 on 2019-07-12 20:50

import datetime
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cources', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amoozeshgah',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='نام آموزشگاه')),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='cource',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cources.Category', verbose_name='دسته بندی دوره'),
        ),
        migrations.AlterField(
            model_name='cource',
            name='date',
            field=models.DateField(default=datetime.date(2019, 7, 12), verbose_name='تاریخ'),
        ),
        migrations.AlterField(
            model_name='cource',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=15, verbose_name='هزینه دوره'),
        ),
        migrations.AddField(
            model_name='amoozeshgah',
            name='category',
            field=models.ManyToManyField(to='cources.Category', verbose_name='دسته بندی آموزش های آموزشگاه'),
        ),
    ]
