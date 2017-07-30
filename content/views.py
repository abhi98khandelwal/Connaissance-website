from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from . import forms


def home(request):
    return render(request, 'content/home.html')

def sponsors(request):
    return render(request, 'content/sponsors.html')

def con16(request):
    return render(request, 'content/con16.html')

def events(request):
    return render(request, 'content/events.html')

def eventp(request):
    form = forms.PhotoForm()
    if request.method == 'POST':
        form = forms.PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save()
            return HttpResponseRedirect(reverse('content:events'))
    return render(request, 'content/eventp.html', {'form':form})

def eventw(request):
    form = forms.WriteForm()
    if request.method == 'POST':
        form = forms.WriteForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save()
            return HttpResponseRedirect(reverse('content:events'))
    return render(request, 'content/eventw.html', {'form':form})