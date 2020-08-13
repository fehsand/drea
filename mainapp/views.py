from django.shortcuts import render

def anasayfa(request):
    return render(request, 'mainapp/anasayfa.html', {})

def hakkimda(request):
    return render(request, 'mainapp/hakkımda.html', {})

def basinda(request):
    return render(request, 'mainapp/basinda.html', {})

def uygulamalar(request):
    return render(request, 'mainapp/uygulamalar.html', {})

def uygulamalar2(request):
    return render(request, 'mainapp/uygulamalar_kirisiklik_tedavisi.html', {})

def uygulamalar3(request):
    return render(request, 'mainapp/uygulamalar_el_ve_koltuk_alti-terleme_tedavisi.html', {})

def uygulamalar4(request):
    return render(request, 'mainapp/uygulamalar_somon_dna_asisi.html', {})

def uygulamalar5(request):
    return render(request, 'mainapp/uygulamalar_aquapeel.html', {})

def uygulamalar6(request):
    return render(request, 'mainapp/uygulamalar_akne_sivilce.html', {})

def uygulamalar7(request):
    return render(request, 'mainapp/uygulamalar_genital_sigil.html', {})

def uygulamalar8(request):
    return render(request, 'mainapp/uygulamalar_mantar_hastaliklari.html', {})

