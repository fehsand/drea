from django.shortcuts import render
from .forms import iletisimForm
from django.utils.translation import gettext_lazy as _

def anasayfa(request):
    return render(request, 'mainapp/anasayfa.html', {})

def hakkimda(request):
    return render(request, 'mainapp/hakkimda.html', {})

def basinda(request):
    return render(request, 'mainapp/basinda.html', {})

def egitim(request):
    return render(request, 'mainapp/egitim.html', {})

def iletisim(response):
    if response.method == "POST":
        form = iletisimForm (response.POST)
        if form.is_valid ():
            isim = form.cleaned_data.get ('isim')
            soy_isim = form.cleaned_data.get ('soy_isim')
            eposta = form.cleaned_data.get ('eposta')
            telefon = form.cleaned_data.get ('telefon')
            ileti = form.cleaned_data.get ('mesaj')
            # ----Tüm kutucukların doldurulması sağlandı yoksa hata verecek---
            if len (isim) < 1 or len (soy_isim) < 1 or len (eposta) < 1 or len (telefon) < 1 or len (ileti) < 1:
                mesaj = _('Kutucukları Doldurunuz.')
                form = iletisimForm ()
                return render (response, 'mainapp/iletisim.html', {'mesaj': mesaj, 'form': form})
            else:
                pass
            # --------------------kutu Kontrolü bitti----------------
            harfler = 'abcçdefgğhıijklmnoöprrsştuüvy z'
            n1=isim.lower()
            n2=soy_isim.lower()
            for harf in n1:
                if not harf in harfler:
                    mesaj = ' : İsim bölümünde Türkçe harfler kullanınız.'
                    return render (response, 'mainapp/iletisim.html', {'n1': n1, 'mesaj': mesaj})
                else:
                    pass
            for harf in n2:
                if not harf in harfler:
                    mesaj = ' : Soy isim bölümünde Türkçe harfler kullanınız.'
                    return render (response, 'mainapp/iletisim.html', {'n2': n2, 'mesaj': mesaj})
                else:
                    pass
            rakamlar='0123456789() +'
            n3=telefon
            for harf in n3:
                if not harf in rakamlar:
                    mesaj = ' : Telefon numaranız rakamlardan oluşmalıdır.'
                    return render (response, 'mainapp/iletisim.html', {'n3': n3, 'mesaj': mesaj})
                else:
                    pass
            form.save ()
            mesaj = _ ("Gönderiniz başarıyla kaydedildi.")
            form = iletisimForm ()
            return render (response, 'mainapp/iletisim.html', {'form': form, 'mesaj': mesaj})
        mesaj = _ ('Lütfen Formu Doldurunuz.')
        return render (response, 'mainapp/iletisim.html', {'form': form, 'mesaj': mesaj})
    else:
        form = iletisimForm ()
        return render (response, 'mainapp/iletisim.html', {'form': form})

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

