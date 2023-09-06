from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'title' : 'Nasya Lib',
        'name': 'Ayu Siti Nasya Ningrum',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)