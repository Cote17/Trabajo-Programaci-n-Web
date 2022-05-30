# Generated by Django 4.0.1 on 2022-05-11 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoCategoria',
            fields=[
                ('idTipoCategoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id')),
                ('nombreTipoCategoria', models.CharField(max_length=50, verbose_name='Tipo de Categoría')),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('idProducto', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id Producto')),
                ('nombre', models.CharField(max_length=20, verbose_name='Nombre producto')),
                ('descripcion', models.CharField(blank=True, max_length=20, null=True, verbose_name='Descripción producto')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.tipocategoria')),
            ],
        ),
    ]