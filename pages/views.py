from django.shortcuts import render, get_object_or_404
from .models import Page


def pages(request, page_id):
    page = get_object_or_404(Page, id=page_id)
    data = {"page": page}
    return render(request, "pages/sample.html", data)
