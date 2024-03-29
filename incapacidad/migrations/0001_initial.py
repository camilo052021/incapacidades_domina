# Generated by Django 3.2.1 on 2021-11-15 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Areas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_area', models.CharField(max_length=255, verbose_name='Nombre Area')),
                ('create_at', models.DateField(auto_now_add=True, null=True, verbose_name='Creado el')),
                ('modify_at', models.DateField(auto_now=True, verbose_name='Actualizado el')),
            ],
            options={
                'verbose_name': 'Nombre Area',
                'verbose_name_plural': 'Areas de la empresa',
            },
        ),
        migrations.CreateModel(
            name='Cargos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cargo', models.CharField(max_length=255, verbose_name='Cargo')),
                ('salario_cargo', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('create_at', models.DateField(auto_now_add=True, null=True, verbose_name='Creado el')),
                ('modify_at', models.DateField(auto_now=True, verbose_name='Actualizado el')),
            ],
            options={
                'verbose_name': 'Cargo',
                'verbose_name_plural': 'Cargos',
            },
        ),
        migrations.CreateModel(
            name='Cie10',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnostico', models.CharField(max_length=4, verbose_name='Código CIE 10')),
                ('grupo', models.TextField(verbose_name='Grupo de Diagnóstico')),
                ('descripcion', models.TextField(verbose_name='Descripción de Diagnóstico')),
            ],
            options={
                'verbose_name': 'Diagnostico',
                'verbose_name_plural': 'Diagnosticos',
            },
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre de Empresa')),
                ('nit', models.CharField(max_length=15, verbose_name='NIT')),
                ('actividad', models.CharField(max_length=255, verbose_name='Actividad Económica')),
                ('nivel_riesgo', models.CharField(max_length=255, verbose_name='Nivel de Riesgo')),
                ('direccion', models.CharField(max_length=255, verbose_name='Dirección')),
                ('ciudad', models.CharField(max_length=255, verbose_name='Ciudad')),
                ('departamento', models.CharField(max_length=255, verbose_name='Departamento')),
                ('cant_trabajadores', models.IntegerField(verbose_name='Cantidad de Trabajadores')),
                ('naturaleza_empresa', models.CharField(max_length=100, verbose_name='Naturaleza jurídica')),
                ('telefonos', models.CharField(max_length=40, verbose_name='Teléfonos de contacto')),
                ('correo', models.EmailField(max_length=255, verbose_name='Correo electrónico')),
                ('tipo', models.CharField(max_length=100, verbose_name='Tipo de empresa')),
                ('create_at', models.DateField(auto_now_add=True, null=True, verbose_name='Creado el')),
                ('modify_at', models.DateField(auto_now=True, verbose_name='Actualizado el')),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresa',
            },
        ),
        migrations.CreateModel(
            name='NivelAcademico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nivel', models.CharField(max_length=255, verbose_name='Nivel Académico')),
                ('create_at', models.DateField(auto_now_add=True, null=True, verbose_name='Creado el')),
                ('modify_at', models.DateField(auto_now=True, verbose_name='Actualizado el')),
            ],
            options={
                'verbose_name': 'Nivel Académico',
                'verbose_name_plural': 'Niveles Académicos',
            },
        ),
        migrations.CreateModel(
            name='Incapacidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origen', models.CharField(max_length=155, verbose_name='Origen')),
                ('clasificacion', models.CharField(max_length=155, verbose_name='Clasificación')),
                ('fecha_inicio', models.DateField(verbose_name='Fecha de Inicio')),
                ('fecha_fin', models.DateField(verbose_name='Fecha de Finalización')),
                ('archivo_inc', models.FileField(default='/static/media/archivos', upload_to='', verbose_name='Cargue el archivo con la incapacidad')),
                ('total_incapacidad', models.IntegerField(verbose_name='Total días incapacidad')),
                ('valor_incapacidad', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Valor Incapacidad')),
                ('valor_asumido_empresa', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Valor Asumido Empresa')),
                ('valor_asumido_eps', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Valor Asumido EPS')),
                ('create_at', models.DateField(auto_now_add=True, verbose_name='Creado el')),
                ('modify_at', models.DateField(auto_now=True, verbose_name='Actualizado el')),
                ('cedula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.profile')),
            ],
            options={
                'verbose_name': 'Incapacidad',
                'verbose_name_plural': 'Incapacidades',
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_ingreso', models.DateField(verbose_name='Fecha de ingreso')),
                ('salario_basico', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Salario')),
                ('arl', models.CharField(max_length=100, verbose_name='ARL')),
                ('tipo_contrato', models.CharField(choices=[('Fijo', 'Fijo'), ('Indefinido', 'Indefinido'), ('Obra Labor', 'Obra Labor'), ('Otro', 'Otro')], max_length=255, verbose_name='Tipo Contrato')),
                ('antiguedad', models.DecimalField(decimal_places=2, max_digits=2, verbose_name='Tiempo en la empresa')),
                ('barrio', models.CharField(default='No indicado', max_length=255, null=True, verbose_name='Barrio')),
                ('ciudad', models.CharField(default='No indicada', max_length=255, verbose_name='Ciudad')),
                ('departamento', models.CharField(default='No indicado', max_length=255, verbose_name='Departamento')),
                ('estrato', models.IntegerField(blank=True, null=True, verbose_name='Estrato')),
                ('create_at', models.DateField(auto_now_add=True, null=True, verbose_name='Creado el')),
                ('modify_at', models.DateField(auto_now=True, verbose_name='Actualizado el')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='incapacidad.areas')),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='incapacidad.cargos')),
                ('cedula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.profile')),
                ('nivel_academico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='incapacidad.nivelacademico')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
            },
        ),
        migrations.AddField(
            model_name='areas',
            name='nit_empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='incapacidad.empresa'),
        ),
    ]
