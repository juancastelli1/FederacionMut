# Generated by Django 3.2 on 2021-09-22 22:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Socios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cobradores',
            fields=[
                ('id_cobrador', models.IntegerField(primary_key=True, serialize=False)),
                ('apellido', models.CharField(max_length=80)),
                ('nombre', models.CharField(max_length=80)),
                ('dni', models.IntegerField(unique=True)),
                ('fecha_cobro', models.DateField()),
                ('realizado', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('numero_socio', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Socios.socios')),
            ],
            options={
                'verbose_name': 'cobrador',
                'verbose_name_plural': 'cobradores',
                'db_table': 'cobradores',
                'ordering': ['id_cobrador'],
            },
        ),
    ]
