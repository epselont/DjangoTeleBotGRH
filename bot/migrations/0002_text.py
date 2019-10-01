# Generated by Django 2.2.5 on 2019-10-01 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=500)),
                ('button', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot.Button')),
            ],
        ),
    ]
