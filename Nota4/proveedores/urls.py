from os import stat
from django.urls import path
from .views import index, crearusuario, form_mod_usuario, ver, form_del_usuario
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path ('', index, name= "index"),
    path('crearusuario/', crearusuario, name="crearusuario"),
    path('ver', ver, name="ver"),
    path('form_del_usuario/<id>', form_del_usuario, name="form_del_usuario"),
    path('form_mod_usuario/<id>',form_mod_usuario, name="form_mod_usuario")
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

