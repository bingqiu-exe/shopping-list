from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Nasywa Kamila Az Zahra',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)