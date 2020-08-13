from django.db import models

class iletisim (models.Model):
    isim = models.CharField(max_length=200, help_text="Lütfen İsminizi Yazınız")
    soy_isim = models.CharField(max_length=200, help_text="Lütfen Soyisminizi Yazınız")
    eposta = models.EmailField(max_length=200, help_text="Lütfen Eposta Adresinizi Yazınız.")
    telefon = models.CharField(max_length=50, help_text="Telefon numaranızı giriniz")
    mesaj = models.TextField(help_text='Mesajınızı yazınız')
    geri_donus = models.BooleanField (default=False, help_text="Cevap verilen mesajlar true yapılacak")
    cevap = models.TextField(null=True, help_text="Cevap metni buraya yazılacak")
    kayit_tarihi = models.DateTimeField(auto_now_add=True)
    guncelleme_tarihi = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.eposta
