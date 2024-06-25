# Generated by Django 5.0.6 on 2024-06-25 13:20

import ckeditor.fields
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SitioWebNoticiasCaos', '0002_articulo_etiquetatitulo_autor_correoelectronico_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='fechaPublicacion',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='articulo',
            name='contenidoArticulo',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
