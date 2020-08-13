from django.urls import path
from . import views

app_name = "mainapp"

urlpatterns = [
    path('', views.anasayfa, name='anasayfa'),
    path('hakkimda-dr-ersin-aydin/', views.hakkimda, name='hakkimda'),
    path('basinda-dr-ersin-aydin/', views.basinda, name='basinda'),
    path('egitim-dr-ersin-aydin/', views.egitim, name='egitim'),
    path('iletisim/', views.iletisim, name='iletisim'),
    path('estetik-kozmetik-ve-genel-dermatoloji-cilt-hastalıkları/', views.uygulamalar, name='uygulamalar'),
    path('estetik-kozmetik-ve-genel-dermatoloji-cilt-hastalıkları/kirisiklik-tedavisi/', views.uygulamalar2, name='uygulamalar2'),
    path('estetik-kozmetik-ve-genel-dermatoloji-cilt-hastalıkları/el-ve-koltuk-alti-terleme-tedavisi/', views.uygulamalar3, name='uygulamalar3'),
    path('estetik-kozmetik-ve-genel-dermatoloji-cilt-hastalıkları/somon-dna-asisi/', views.uygulamalar4, name='uygulamalar4'),
    path('estetik-kozmetik-ve-genel-dermatoloji-cilt-hastalıkları/aquapeel/', views.uygulamalar5, name='uygulamalar5'),
    path('estetik-kozmetik-ve-genel-dermatoloji-cilt-hastalıkları/akne-sivilce/', views.uygulamalar6, name='uygulamalar6'),
    path('estetik-kozmetik-ve-genel-dermatoloji-cilt-hastalıkları/genital-sigil/', views.uygulamalar7, name='uygulamalar7'),
    path('estetik-kozmetik-ve-genel-dermatoloji-cilt-hastalıkları/mantar-hastaliklari/', views.uygulamalar8, name='uygulamalar8'),
]
