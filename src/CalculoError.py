#!/usr/bin/python
#! encoding: UTF-8
import time
import timeit
import modulo_1
start=time.time()
l=[]
def error(intervalos,test,umbral):
  fallos=0
  for i in range (test):
    s=modulo_1.aproxpi(intervalos)
    error=abs(s-modulo_1.pi)
    if error>=umbral:
      fallos=fallos+1
  return ((fallos/test)*100)
if __name__=="__main__":
   import sys
   if (len(sys.argv)==4):
     p1=int(sys.argv[1])
     p2=int(sys.argv[2])
     p3=float(sys.argv[3])
   else:
     print "El programa se ejecutará por defecto con los valores 10 10 0.1 ,ya que usted no ha introducido los parametros en la linea de comando "
     p1=10
     p2=10
     p3=0.1
   s=error(p1,p2,p3)
   print "El porcentaje de error es de: %5.3f" %s
   finish=time.time()-start
   print "El tiempo que tarda en realizarse el proceso es: %14.13f" %finish
   l=l+[finish]
   print "Proporcione un nombre para el fichero donde se guardarán los resultados:"
   nombre_fichero= raw_input();
   f=open(nombre_fichero, 'w')
   f.write('El tiempo tardado es de:')
   f.write(str(l[0]) + '\n')
   f.close()