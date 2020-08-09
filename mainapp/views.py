from django.shortcuts import render

def anasayfa(request):
    return render(request, 'mainapp/anasayfa.html', {})

