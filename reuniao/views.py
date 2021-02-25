from django.shortcuts import render, get_object_or_404, redirect
from .forms import ReuniaoForm
from django.http import HttpResponse
from .models import Reuniao
from django.contrib import messages

def reuniaoList(request):

     search = request.GET.get('search')
     filter = request.GET.get('filter')

     if search:

          reuniao = Reuniao.objects.filter(name__icontains=search)


     elif filter:

          reuniao = Reuniao.objects.filter(serie=filter)

     else:

          reuniao = Reuniao.objects.all()[:0]

     return render(request, 'reuniao/presenca.html', {'reuniao': reuniao})

def reuniaoView(request, id):
     reuniao = get_object_or_404(Reuniao, pk=id)
     return render(request, 'reuniao/aluno.html', {'reuniao': reuniao})

def saveView(request, id):
     reuniao = get_object_or_404(Reuniao, pk=id)
     print(reuniao)
     if(reuniao.ausente == 'ausente'):
          reuniao.ausente = 'presente'

          reuniao.save()
     
     messages.info(request, 'Salvo!')

     return redirect('/')

