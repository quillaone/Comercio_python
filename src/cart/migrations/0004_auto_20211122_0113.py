# Generated by Django 3.0.8 on 2021-11-22 01:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_auto_20200709_2236'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.CharField(default='0', max_length=150)),
                ('imagen', models.ImageField(upload_to='producto_images')),
                ('descripcion', models.TextField()),
                ('precio', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=False)),
                ('cantidad_en_stock', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='available_colours',
        ),
        migrations.RemoveField(
            model_name='product',
            name='available_sizes',
        ),
        migrations.RemoveField(
            model_name='product',
            name='primary_category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='secondary_categories',
        ),
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name_plural': 'Direcciones'},
        ),
        migrations.RemoveField(
            model_name='address',
            name='zip_code',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='colour',
        ),
        migrations.RenameModel(
            old_name='ColourVariation',
            new_name='Medida',
        ),
        migrations.DeleteModel(
            name='SizeVariation',
        ),
        migrations.AddField(
            model_name='producto',
            name='cantidad',
            field=models.ManyToManyField(to='cart.Medida'),
        ),
        migrations.AddField(
            model_name='producto',
            name='categoria_primaria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='primary_productos', to='cart.Category'),
        ),
        migrations.AddField(
            model_name='producto',
            name='subcategoria',
            field=models.ManyToManyField(blank=True, to='cart.Category'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.Producto'),
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
