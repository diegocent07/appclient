# Generated by Django 3.0.6 on 2020-09-11 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0010_auto_20200909_0841'),
    ]

    operations = [
        migrations.AddField(
            model_name='datosclientes',
            name='docladoa',
            field=models.FileField(default=0, upload_to='images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='datosclientes',
            name='docladob',
            field=models.FileField(default=0, upload_to='images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='datosclientes',
            name='email',
            field=models.EmailField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='datosclientes',
            name='telefono',
            field=models.CharField(default=0, max_length=25),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='datosclientes',
            name='Docnro',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='datosclientes',
            name='comprobantep',
            field=models.FileField(default=0, upload_to='images/'),
            preserve_default=False,
        ),
    ]