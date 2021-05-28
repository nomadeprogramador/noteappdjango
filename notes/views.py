from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Note
# Create your views here.
def index (request):
    notes = Note.objects.all()
    context = {
        'notes':notes,
    }
    return render (request,'noteapp/index.html',context)
def notas_marcadas(request):
    notas_marcadas=Note.objects.filter(marcado=True)
    context={
        'notas_marcadas':notas_marcadas,
    }
    return render (request,'noteapp/marcados.html',context)
def excluir_nota(request,id):
    note=Note.objects.get(id=id)
    note.delete()
    return redirect ('index')