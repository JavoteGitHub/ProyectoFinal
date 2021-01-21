from django.contrib import admin
from .models import TejidoMama

# Register your models here.

class TejidoMamaAdmin(admin.ModelAdmin):
   list_display = ('partP','temperatura','color','inflamacion',)
 

admin.site.register(TejidoMama,TejidoMamaAdmin)

#class GrafoAdmin(admin.ModelAdmin):
#pass
#""" list_display = ('origen', 'destino', 'conectado') """   
#admin.site.register(Grafo, GrafoAdmin)