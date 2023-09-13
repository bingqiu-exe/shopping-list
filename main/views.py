from django.shortcuts import render

def show_main(request):
    context = {
        'Name of Sponsor',
        'Kim Dokja'
    }

    return render(request, "main.html", context)