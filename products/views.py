"""
A view function, or view for short, is a Python function that
takes a Web request and returns a Web response. This response
can be the HTML contents of a Web page, or a redirect, or a
404 error, or an XML document, or an image . . . or anything, really.
"""

from django.core.paginator import Paginator, Page
from django.db.models.query import QuerySet
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse

from products.forms import ProductForm, ProductNutrientForm
from products.models import Product, Status, ProductNutrient


def product_list_view(request: HttpRequest) -> HttpResponse:
    """
    Endpoint for listing, searching and creating Products.
    """
    # Handling the Product creation form.
    form: ProductForm = ProductForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(reverse("products.list"))
    # Listing all Products.
    products: QuerySet = Product.objects.all()
    # Filtering by Product status.
    status: str = request.GET.get('status', '')
    if status:
        products = products.filter(status=status)
    # Filtering by product Name.
    name: str = request.GET.get('name', '')
    if name:
        products = products.filter(name__icontains=name)
    # Pagination.
    size: int = int(request.GET.get('size', 10))
    offset: int = int(request.GET.get('offset', 1))
    paginator: Paginator = Paginator(products, size)
    page: Page = paginator.page(offset)
    # Rendering Product list.
    return render(request, "products.html", {
        'form': form,
        'offset': offset,
        'size': size,
        'page': page,
        'Status': Status,
        'status': status,
        'name': name,
    })


def product_details_view(request: HttpRequest,
                         product_pk: int) -> HttpResponse:
    """
    Endpoint for describing, updating and deleting a Product.
    """
    # Loading Product by ID (or raising error).
    product: Product = Product.objects.get(pk=product_pk)
    # Handling the form to update the Product.
    form: ProductForm = ProductForm(request.POST or None,
                                    instance=product)
    if request.method == "POST":
        if request.POST.get("__delete"):
            # Deleting Product by ID.
            product.delete()
            return redirect(reverse("products.list"))
        elif form.is_valid():
            # Updating Product by ID.
            form.save()
            return redirect(reverse("products.list"))
    return render(request, "product.html", {
        'form': form,
        'product': product,
    })


def product_nutrients_list_view(request: HttpRequest,
                                product_pk: int) -> HttpResponse:
    """
    Endpoint for listing, searching and creating Products Nutrients.
    """
    # Loading Product by ID (or raising error).
    product: Product = Product.objects.get(pk=product_pk)
    # Handling the Product creation form.
    form: ProductNutrientForm = ProductNutrientForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(reverse("products.nutrients.list",
                                    kwargs={'product_pk': product_pk}))
    # Listing all Nutrients. Pagination is undesired.
    nutrients: QuerySet = product.nutrients.all()
    # Rendering Product list.
    return render(request, "product_nutrients.html", {
        'form': form,
        'product': product,
        'nutrients': nutrients,
    })


def product_nutrient_details_view(request: HttpRequest,
                                  product_pk: int,
                                  nutrient_pk: int) -> HttpResponse:
    """
    Endpoint for describing, updating and deleting a Product.
    """
    # Loading Product Nutrient by ID (or raising error).
    nutrient: ProductNutrient = ProductNutrient.objects.get(nutrient__pk=nutrient_pk,
                                                            product__pk=product_pk)
    # Handling the form to update the Product.
    form: ProductNutrientForm = ProductNutrientForm(request.POST or None,
                                                    instance=nutrient)
    if request.method == "POST":
        if request.POST.get("__delete"):
            # Deleting Product Nutrient by ID.
            nutrient.delete()
            return redirect(reverse("products.nutrients.list",
                                    kwargs={'product_pk': product_pk}))
        elif form.is_valid():
            # Updating Product Nutrient by ID.
            form.save()
            return redirect(reverse("products.nutrients.details",
                                    kwargs={
                                        'nutrient_pk': nutrient_pk,
                                        'product_pk': product_pk,
                                    }))
    # Handling Product Nutrients.
    form: ProductNutrientForm = ProductNutrientForm(request.POST or None)
    # Handling the Product creation form.
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(reverse("products.list"))
    return render(request, "product_nutrient.html", {
        'form': form,
        'nutrient': nutrient,
    })
