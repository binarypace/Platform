from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def AboutusView(request):
	return HttpResponse(' Know About us  !!!')
