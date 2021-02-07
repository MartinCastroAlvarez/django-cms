"""
A view function, or view for short, is a Python function that
takes a Web request and returns a Web response. This response
can be the HTML contents of a Web page, or a redirect, or a
404 error, or an XML document, or an image . . . or anything, really.
"""

from django.core.paginator import Paginator
from django.db.models.query import QuerySet
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse

from nutrients.forms import NutrientForm
from nutrients.models import Nutrient, Unit


def nutrient_list_view(request: HttpRequest) -> HttpResponse:
    """
    Endpoint for listing, searching and creating Nutrients.
    """
    # Handling the Nutrient creation form.
    form: NutrientForm = NutrientForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(reverse("nutrients.list"))
    # Listing all Nutrients.
    nutrients: QuerySet = Nutrient.objects.all()
    # Filtering by nutrient Name.
    name: str = request.GET.get('name', '')
    if name:
        nutrients = nutrients.filter(name__icontains=name)
    # Pagination.
    size: int = int(request.GET.get('size', 10))
    offset: int = int(request.GET.get('offset', 1))
    paginator: Paginator = Paginator(nutrients, size)
    page: Page = paginator.page(offset)
    # Rendering Nutrient list.
    return render(request, "nutrients.html", {
        'form': form,
        'offset': offset,
        'size': size,
        'page': page,
        'name': name,
    })


def nutrient_details_view(request: HttpRequest,
                          nutrient_pk: int) -> HttpResponse:
    """
    Endpoint for describing, updating and deleting a Nutrient.
    """
    # Loading Nutrient by ID (or raising error).
    nutrient: Nutrient = Nutrient.objects.get(pk=nutrient_pk)
    # Handling the form to update the .Nutrient
    form: NutrientForm = NutrientForm(request.POST or None,
                                      instance=nutrient)
    if request.method == "POST":
        if request.POST.get("__delete"):
            # Deleting Nutrient by ID.
            nutrient.delete()
            return redirect(reverse("nutrients.list"))
        elif form.is_valid():
            # Updating Nutrient by ID.
            form.save()
            return redirect(reverse("nutrients.list"))
    return render(request, "nutrient.html", {
        'form': form,
        'nutrient': nutrient,
    })
