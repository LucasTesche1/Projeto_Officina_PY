# Generated by Django 5.1 on 2024-10-07 16:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0002_alter_carro_placa'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaManutencao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(choices=[('TVM', 'Trocar válvula do motor'), ('TO', 'Trocar o óleo'), ('B', 'Balanceamento'), ('A', 'Alinhamento'), ('TP', 'Trocar pneu'), ('RF', 'Revisão dos freios'), ('TB', 'Trocar bateria'), ('LBI', 'Limpeza de bico injetor'), ('TC', 'Trocar correia dentada'), ('VS', 'Verificação de suspensão'), ('TA', 'Trocar amortecedor'), ('TFA', 'Trocar filtro de ar'), ('TFC', 'Trocar filtro de combustível'), ('TPF', 'Trocar pastilha de freio'), ('RE', 'Regulagem de embreagem'), ('AF', 'Alinhamento do farol'), ('RAC', 'Reparo no ar condicionado'), ('TL', 'Troca de lâmpadas')], max_length=3)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('data_inicio', models.DateField(null=True)),
                ('data_entrega', models.DateField(null=True)),
                ('finalizado', models.BooleanField(default=False)),
                ('protocolo', models.CharField(blank=True, max_length=32, null=True)),
                ('categoria_manutencao', models.ManyToManyField(to='servicos.categoriamanutencao')),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clientes.cliente')),
            ],
        ),
    ]