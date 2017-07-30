from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from . import forms
from .models import PEvent, WEvent
import os


def home(request):
    return render(request, 'content/home.html')

def sponsors(request):
    return render(request, 'content/sponsors.html')

def con16(request):
    return render(request, 'content/con16.html')


def eventp(request):
