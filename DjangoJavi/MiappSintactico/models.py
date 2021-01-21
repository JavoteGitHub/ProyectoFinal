from django.db import models

class TejidoMama(models.Model):
    partP = models.IntegerField()
    temperatura = models.FloatField()
    color = models.FloatField()
    inflamacion = models.FloatField()

class Grafo(models.Model):
      origen =models.ForeignKey(TejidoMama, on_delete=models.CASCADE,  related_name='origen')      
      destino = models. ForeignKey(TejidoMama, on_delete =models.CASCADE, related_name='destino')      
      conectado = models.BooleanField()
      
def __str__(self):
          Registro1 = str(self.origen.partP)+', '+str(self.origen.temperatura)+','+str(self.origen.inflamacion)
          Registro2 = str(self.destino.partP)+','+str(self.destino.temperatura)+','+str(self.destino.inflamacion)
          return Registro1+'-'+Registro2 
   