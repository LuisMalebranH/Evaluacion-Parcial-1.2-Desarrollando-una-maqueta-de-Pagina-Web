# Generated by Django 5.0.6 on 2024-06-26 21:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SitioWebNoticiasCaos', '0006_alter_articulo_imagenarticulo_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='usuarioEditor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='articulos_editor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='usuarioAutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articulos_autor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Editor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priNomEditor', models.CharField(max_length=15)),
                ('segNomEditor', models.CharField(max_length=15)),
                ('apPaternoEditor', models.CharField(max_length=15)),
                ('apMaternoEditor', models.CharField(max_length=15)),
                ('fonoEditor', models.CharField(max_length=11)),
                ('correoElectronico', models.CharField(default='example@email.com', max_length=40)),
                ('usuarioEditor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
