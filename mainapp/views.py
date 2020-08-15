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

def uygulamalar9(request):
    return render(request, 'mainapp/uygulamalar_lazer_uygulamalari.html', {})

def uygulamalar10(request):
    return render(request, 'mainapp/uygulamalar_cosmelan_dermamelan_leke_tedavisi.html', {})

def uygulamalar11(request):
    return render(request, 'mainapp/uygulamalar_peeling.html', {})

def uygulamalar12(request):
    return render(request, 'mainapp/uygulamalar_dis_sikma_tedavisi.html', {})

def uygulamalar13(request):
    return render(request, 'mainapp/uygulamalar_ip_uygulamasi.html', {})

def uygulamalar14(request):
    return render(request, 'mainapp/uygulamalar_dolgu_uygulamalari.html', {})

def uygulamalar15(request):
    return render(request, 'mainapp/uygulamalar_sac_mezoterapisi.html', {})

def uygulamalar16(request):
    return render(request, 'mainapp/uygulamalar_fraksiyonel-radyofrekans-altin-igne.html', {})

def uygulamalar17(request):
    return render(request, 'mainapp/uygulamalar_roller-ve-dermapen.html', {})

def uygulamalar18(request):
    return render(request, 'mainapp/uygulamalar_prp-platelet-rich-plasma.html', {})

def uygulamalar19(request):
    return render(request, 'mainapp/uygulamalar_cilt-bakimi.html', {})

def uygulamalar20(request):
    return render(request, 'mainapp/uygulamalar_mezoterapi.html', {})

def uygulamalar21(request):
    return render(request, 'mainapp/uygulamalar_leke-tedavisi.html', {})

def uygulamalar22(request):
    return render(request, 'mainapp/uygulamalar_behcet-hastaligi.html', {})

def uygulamalar23(request):
    return render(request, 'mainapp/uygulamalar_cinsel-yolla-bulasan-hastaliklar.html', {})

def uygulamalar24(request):
    return render(request, 'mainapp/uygulamalar_cilt-benleri.html', {})

def uygulamalar25(request):
    return render(request, 'mainapp/uygulamalar_cilt-kanserleri.html', {})

def uygulamalar26(request):
    return render(request, 'mainapp/uygulamalar_ekzema.html', {})

def uygulamalar27(request):
    return render(request, 'mainapp/uygulamalar_sigil-verru.html', {})

def uygulamalar28(request):
    return render(request, 'mainapp/uygulamalar_urtiker-kurdesen.html', {})

def uygulamalar29(request):
    return render(request, 'mainapp/uygulamalar_gunesten-korunma.html', {})

def uygulamalar30(request):
    return render(request, 'mainapp/uygulamalar_herpes-simpleks-enfeksiyonu-ucuk.html', {})

def uygulamalar31(request):
    return render(request, 'mainapp/uygulamalar_hiperhidrozis-asiri-terleme.html', {})

def uygulamalar32(request):
    return render(request, 'mainapp/uygulamalar_hipertrofik-skar-keloid.html', {})

def uygulamalar33(request):
    return render(request, 'mainapp/uygulamalar_liken-planus.html', {})

def uygulamalar34(request):
    return render(request, 'mainapp/uygulamalar_tirnak-hastaliklari.html', {})

def uygulamalar35(request):
    return render(request, 'mainapp/uygulamalar_vitiligo.html', {})

def uygulamalar36(request):
    return render(request, 'mainapp/uygulamalar_pitriazis-rosea.html', {})

def uygulamalar37(request):
    return render(request, 'mainapp/uygulamalar_psoriazis-sedef-hastaligi.html', {})

def uygulamalar38(request):
    return render(request, 'mainapp/uygulamalar_roza-hastaligi-gul-hastaligi-gulleme.html', {})

def uygulamalar39(request):
    return render(request, 'mainapp/uygulamalar_sac-hastaliklari.html', {})

def uygulamalar40(request):
    return render(request, 'mainapp/uygulamalar_sac-dokulmesi.html', {})

def uygulamalar41(request):
    return render(request, 'mainapp/uygulamalar_zona-zoster-gece-yanigi.html', {})



