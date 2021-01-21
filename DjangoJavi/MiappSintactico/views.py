from django.shortcuts import render
from django.http import HttpResponse
from .models import TejidoMama
from django_pandas.io import read_frame
import pandas as pd

#import networkx as nx
#import matplotlib.pyplot as plt
#import mpld3


# Create your views here.
def home(request): 
   return render(request,'MiappSintactico/home.html')
   
def cancer(request):
   partesTejido = TejidoMama.objects.all()   
   procesado= procesa_tabla(partesTejido)
   return render(request, 'MiAppSintactico/cancer.html', {'tabla': partesTejido,'proceso': procesado})

def tabla(request):    
   partesTejido = TejidoMama.objects.all()   #CONSULTA A BBD O QUERY SET
   return render(request, 'MiAppSintactico/tabla.html', {'tabla': partesTejido}) #DICCIONARIO DE CONTEXTO

def grafo(request):    

   return render(request, 'MiAppSintactico/grafo.html')   

def procesa_tabla(tabla):
       
   df= read_frame(tabla)   
   for item in tabla: 
      print(item.temperatura) 
   for item in tabla: 
      print(item.color)   
   for item in tabla: 
      print(item.inflamacion) 

   print(df)  
   
   return "Mi proceso"  


def procesaTabla(request):
   tejido = CaracteristicasTejidoMama.objects.all()
   df = read_frame(tejido) 
   mtempera = df['temperatura'].mean() 
   mcolor = df['color'].mean() 
   mflama = df['inflamacion'].mean() 

   protemp = df['temperatura'].mean() 
   procolor = df['color'].mean() 
   proinfla = df['inflamacion'].mean()
      
   destemp = df['temperatura'].std()
   descolor = df['color'].std() 
   desinfla = df['inflamacion'].std() 
    
   maxtemp = df ['temperatura'].max()
   maxcolor = df ['color'].max()
   maxflama = df ['inflamacion'].max()
    
   mintemp = df ['temperatura'].min()
   mincol = df ['color'].min()
   mininfla = df ['inflamacion'].min()
       
   datos = {'mtempera': mtempera, 'procolor':procolor, 'proinfla':proinfla, 'stdtemperatura':destemp, 'stdcolor':descolor, 'stdinflamacion':desinfla, 'maxt':maxtemp, 'maxc': maxcolor,'maxi':maxflama , 'minimotem':mintemp,'minicolor':minicol,'minimoinfla':mininfla} 
   datos['modatem']=df['temperatura'].median()
   datos['modacolor']= df['color'].median()
   datos['modainfla']= df['inflamacion'].median()
   print(df)
   return render(request, 'MiAppSintactico/tabla.html', datos)



   