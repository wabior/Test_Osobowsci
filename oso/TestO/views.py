from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from .models import *

def index(request):
    pytania = Pytanie.objects.all()
    context = {'pytania': pytania}
    return render(request,'INDEX.html',context)


def detail(request,Pytanie_id):
    ile = Pytanie.objects.count()
    nr_pytania = Pytanie.objects.get(pk=Pytanie_id)
    odps = Odp2.objects.all()
    return render(request, 'detail.html',{'odps':odps,'nr_pytania':nr_pytania,'ile':ile,})

def Zapisz(request, Pytanie_id):
    nr_pytania = Pytanie.objects.get(pk=Pytanie_id)
    selected_Odp = Odp2.objects.get(pk=request.POST['o'])
    selected_Odp.licznik += 1
    selected_Odp.save()

    return HttpResponseRedirect(reverse('results', args=(Pytanie_id,)))

def Zapisz2(request, Pytanie_id):
    ile = Pytanie.objects.count()
    odps = Odp2.objects.all()
    nr_pytania = get_object_or_404(Pytanie, pk=Pytanie_id)
    try:
        selected_Odp = Odp2.objects.get(pk=request.POST['o'])

    except (KeyError, Odp2.DoesNotExist):
        return render(request,'detail.html' , {'odps':odps,'nr_pytania':nr_pytania,'ile':ile,
                                               'error_message': "You didn't select a choice.",})
    else:
        selected_Odp.licznik += 1
        selected_Odp.save()
    # nr_pytania = Pytanie.objects.get(pk=Pytanie_id)

    return render(request,'detail.html' , {'odps':odps,'nr_pytania':nr_pytania,'ile':ile,})


def results(request, Pytanie_id):
    ile = Pytanie.objects.count()
    nr_pyt =  Pytanie_id
    odps = Odp2.objects.all()
    return render(request, 'results.html', {'nr_pyt': nr_pyt, 'odps':odps,'ile':ile,})

def wynik(request):
    return render(request,'wynik.html',{})

def wynik2(request):
    return render(request,'wynik2.html',{})