from django.shortcuts import render
from django.http import HttpResponse
from .models import wishlistModel


# Create your views here.
def wishlistView(request):
	#return HttpResponse('Whats your wishlist for life !!!')
	all_wishlistModel = wishlistModel.objects.all()
	 return render (request,'wishlist.html',{'all_wish': all_wishlistModel })