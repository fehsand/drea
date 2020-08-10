from django.urls import path, include
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
]

urlpatterns += i18n_patterns(
    path('', include('mainapp.urls')),
    prefix_default_language=False,
)

