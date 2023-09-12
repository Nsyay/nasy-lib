from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name' : 'The 48 Laws of Power',
        'author' : 'Robert Greene',
        'amount' : 48,
        'genre' : 'non-fiction',
        'description' : 'evil book'
    }

    return render(request, "main.html", context)