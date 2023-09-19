from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core import serializers
from main.forms import BookForm
from django.urls import reverse
from django.shortcuts import render
from main.models import Book


# Create your views here.
def show_main(request):
    books = Book.objects.all()
    context = {
        'books' : books
    }

    return render(request, "main.html", context)

def book_entry(request):
    form = BookForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "book_entry.html", context)

def show_xml(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Book.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")\

def show_json_by_id(request, id):
    data = Book.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")