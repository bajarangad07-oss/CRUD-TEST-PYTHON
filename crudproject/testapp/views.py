from django.shortcuts import render,redirect,get_object_or_404,get_list_or_404
from .models import Product
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator

def product_list(request):
    product = Product.objects.all().order_by('id')
    search = request.GET.get('search')
    if search:
        product = product.filter(product_name__icontains=search)
    paginator = Paginator(product, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'product_list.html',{'page_obj': page_obj,'search': search})

def product_add(request):
    if request.method == "POST":
        product = Product(
            product_name=request.POST.get("product_name", "").strip(),
            category=request.POST.get("category", "").strip(),
            price=request.POST.get("price", "").strip() or None,
            quantity=request.POST.get("quantity", "").strip() or None,
            supplier=request.POST.get("supplier", "").strip(),
            minimum_stock_level=request.POST.get("minimum_stock_level", "").strip() or None,
        )

        try:
            product.full_clean()
            product.save()
            return redirect("product_list")
        except ValidationError as e:
            return render(request,"product_add.html",{"errors": e.message_dict,"product": product})

    return render(request, "product_add.html")

def product_edit(request,id):
    product=get_object_or_404(Product,id=id)
    if request.method == "POST":
        product.product_name=request.POST.get("product_name")
        product.category=request.POST.get("category")
        product.price=request.POST.get("price")
        product.quantity=request.POST.get("quantity")
        product.supplier=request.POST.get("supplier")
        product.minimum_stock_level=request.POST.get("minimum_stock_level")
        product.save()
        return redirect('product_list')
    return render(request,'product_edit.html',{'product':product})


def product_delete(request,id):
    product=get_object_or_404(Product,id=id)
    product.delete()
    return redirect('product_list')
