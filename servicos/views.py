from contextlib import nullcontext
from django.http import HttpResponse, FileResponse
from django.shortcuts import render,get_object_or_404
from .models import Servico
from .forms import FormServico
from fpdf import FPDF
from io import BytesIO


# Create your views here.
def novo_servico(request):
    if request.method == 'GET':
        form = FormServico()
        return render(request, 'novo_servico.html', {'form': form})

    elif request.method == 'POST':
        form = FormServico(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse('Salvo com sucesso')

        else:
            return render(request, 'novo_servico.html', {'form': form})


def listar_servico(request):
    if request.method == 'GET':
        servicos = Servico.objects.all()
        return render(request, 'listar_servico.html', {'servicos': servicos})


def servico(request, identificador):
    servico = get_object_or_404(Servico, identificador=identificador)

    return render (request, 'servico.html', {'servico': servico})

def gerar_os(request, identificador):
    servico = get_object_or_404(Servico, identificador=identificador)
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font('Arial', 'B', size=11)

    pdf.set_fill_color(240,240,240)
    pdf.cell(35,10,'Cliente:', 1, 0, 'L', True)
    pdf.cell(0,10,f'{servico.cliente.nome}', 1, 1, 'L', True)

    pdf.cell(35,10,'Manutenções:', 1, 0, 'L', True)

    categorias_manutencao = servico.categoria_manutencao.all()
    for i, manutencao in enumerate(categorias_manutencao):

        pdf.cell(0,10,f'- {manutencao.get_titulo_display()}', 1, 1, 'L', True)
        if not i == len(categorias_manutencao) -1:
            pdf.cell(35,10,'',0,0)

    pdf.cell(35,10,'Valor total:', 1, 0, 'L', True)
    pdf.cell(35,10,f'{servico.preco_total()}',1,1,'L',False)

    pdf.cell(35,10,'Data de início:', 1, 0, 'L', True)
    pdf.cell(0,10,f'{servico.data_inicio}',1,1,'L',True)
    pdf.cell(35,10,'Data de entrega:', 1, 0, 'L', True)
    pdf.cell(0,10,f'{servico.data_entrega}',1,1,'L',True)

    pdf.cell(35,10,'Protocolo:', 1, 0, 'L', True)
    pdf.cell(35,10,f'{servico.protocolo}',0,1,'L',False)

    pdf_content = pdf.output(dest='S').encode('latin')

    pdf_bytes = BytesIO(pdf_content)

    return FileResponse(pdf_bytes, filename=f'os-{servico.protocolo}.pdf')
