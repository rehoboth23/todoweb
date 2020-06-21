# Generated by Django 3.0.7 on 2020-06-19 21:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20200619_2142'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('made', models.DateField(auto_now_add=True)),
                ('warning', models.DateField(blank=True, null=True)),
                ('done', models.DateField(blank=True, null=True)),
                ('memo', models.TextField()),
                ('important', models.BooleanField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Todo_List',
        ),
    ]
