from django.shortcuts import render

def show_main(request):
    name = {'Kim Dokja'}
    amount = {'Insert Amount of Sponsors.'}


    return render(request, "main.html", name, amount)