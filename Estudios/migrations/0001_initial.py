# Generated by Django 3.2 on 2021-09-28 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='estudios',
            fields=[
                ('id_estudio', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(choices=[('Oftalmologia', '1- Oftalmología'), ('Optica', '2- Óptica'), ('Analisis bioquimico', '3- Análisis bioquímico'), ('Odontologia', '4- Odontología'), ('Diag. Imagenes', '5- Diag. Imágenes')], max_length=60)),
                ('cod_estudio', models.CharField(max_length=30)),
                ('abreviatura', models.CharField(max_length=30, null=True)),
                ('UB', models.DecimalField(decimal_places=2, max_digits=8, null=True)),
                ('activo', models.BooleanField(default=True)),
                ('descripcion', models.CharField(max_length=60)),
                ('denominación', models.CharField(max_length=30, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'estudio',
                'verbose_name_plural': 'estudios',
                'db_table': 'estudios',
                'ordering': ['id_estudio'],
            },
        ),
    ]
