import datetime
import json
from django.http import HttpResponseRedirect, JsonResponse
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from main.forms import BookForm
from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import redirect
from main.models import Book
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    books = Book.objects.filter(user=request.user)
    quant = Book.objects.filter(user=request.user).count()
    context = {
        'name' : request.user.username,
        'books' : books,
        'quant' : quant,
        'last_login' : request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

def book_entry(request):
    form = BookForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        book = form.save(commit = False)
        book.user = request.user
        book.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "book_entry.html", context)

def book_delete(request, pk):
    book = Book.objects.get(id=pk)
    book.delete()
    return HttpResponseRedirect('/')

def add_amount(request, pk):
    book = Book.objects.get(id=pk)
    book.amount += 1
    book.save()
    return HttpResponseRedirect('/')

def sub_amount(request, pk):
    book = Book.objects.get(id=pk)
    if book.amount != 0 :
        book.amount -= 1
    book.save()
    return HttpResponseRedirect('/')

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been successfully created!")
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

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

def get_book_json(request):
    book_item = Book.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', book_item))

@csrf_exempt
def create_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        author = request.POST.get("author")
        genre = request.POST.get("genre")
        description = request.POST.get("description")
        user = request.user

        book_entry = Book(name=name, amount=amount, author=author, genre=genre, description=description, user=user)
        book_entry.save()

        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_product = Book.objects.create(
            user = request.user,
            name = data["title"],
            amount = int(data["amount"]),
            author = data["author"],
            genre = data["genre"],
            description = data["description"]
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)