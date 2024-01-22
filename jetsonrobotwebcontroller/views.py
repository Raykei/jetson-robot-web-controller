from django.shortcuts import render

def app(request):
    context = {}
    return render(request, "main.html", context)