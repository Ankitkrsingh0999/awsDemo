from django.shortcuts import render
from .models import Product

from .forms import ProductForm, RawProductionForm
# Create your views here.

#def product_create_view(request):
#	my_form = RawProductionForm()
#	if request.method == "POST":
#		my_form = RawProductionForm(request.POST)
#		if my_form.is_valid():
#			print(my_form.cleaned_data)
#		else:
#			print(my_form.errors)
#	context = {
#		"form": my_form
#	}
#	return render(request, "products/product_create.html" , context)







def product_create_view(request):
	form = ProductForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ProductForm()
	context = {
		'form' : form
	}
	return render(request, "products/product_create.html" , context)

def product_detail_view(request):
	obj=Product.objects.get(id=1)
	context = {
		'object' : obj
	}
	return render(request, "products/product_detail.html" , context)