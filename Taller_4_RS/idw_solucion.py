import time
start_Totaltime = time.time()
import numpy as np
import gdal
import os
import osr
from gdalconst import *
#import matplotlib.pyplot as plt
from collections import Counter
nortes,estes,cotas,profundidad,porosidad=np.loadtxt('PuntosTaller4.csv',dtype={'names':('norte','este','cota','profundidad','porosidad'),'formats':('f4','f4','f4','f4','f2')},delimiter=';',usecols=(0,1,2,3,4),unpack=True,skiprows=1)

def fill(z):
    arr=np.empty((1001,1001))
    arr[:]=np.pi
    for k in range(len(nortes)):
        x=estes[k]
        y=1000-nortes[k]
        arr[y,x]=z[k]
    return arr



#%%

#%%
def h(x1, x2, y1, y2):
    return np.sqrt((x1-x2)**2+(y1-y2)**2)


#%%    

def idwinterp(z, n):
    
    for i in range(1001):
        este=i
        for j in range(1001):
            norte=1000-j
            totalInvDistancia=0
            if z[j,i]==np.pi:
                num=0
                den=0
                for k in range(len(nortes)):
                    weight=np.round(h(norte, nortes[k], este, estes[k]))**-n
                    num+=weight*z[1000-nortes[k], estes[k]]
                    den+=weight
                    z[j,i]=num/den
            else:
                pass
            
    
                
    return plt.imshow(z, interpolation='none')

#%%
import matplotlib.pyplot as plt
plt.figure(4)
cot_arr_2=fill(cotas)
start_time = time.time()
idwinterp(cot_arr_2, 2)
plt.colorbar()
print("It took me %s seconds." % (time.time() - start_time))
plt.gcf()
plt.savefig('cota.png')
#plt.show()


#%%
plt.figure(5)
prf_arr_2=fill(profundidad)
start_time = time.time()
idwinterp(prf_arr_2, 2)
plt.colorbar()
print("It took me %s seconds." % (time.time() - start_time))
plt.gcf()
plt.savefig('profundidad.png')
#plt.show()
#%%

plt.figure(6)
por_arr_2=fill(porosidad)
start_time = time.time()
idwinterp(por_arr_2, 2)
plt.colorbar()
print("It took me %s seconds." % (time.time() - start_time))
plt.gcf()
plt.savefig('porosidad.png')
#plt.show()
#%%
plt.figure(7)
cot_arr_4=fill(cotas)
start_time = time.time()
idwinterp(cot_arr_4, 4)
plt.colorbar()
print("It took me %s seconds." % (time.time() - start_time))
plt.gcf()
plt.savefig('cota_4.png')
#plt.show()
#%%

plt.figure(8)
prf_arr_4=fill(profundidad)
start_time = time.time()
idwinterp(prf_arr_4, 4)
plt.colorbar()
print("It took me %s seconds." % (time.time() - start_time))
plt.gcf()
plt.savefig('profundidad_4.png')
#plt.show()
#%%

plt.figure(9)
por_arr_4=fill(porosidad)
start_time = time.time()
idwinterp(por_arr_4, 4)
plt.colorbar()
print("It took me %s seconds." % (time.time() - start_time))
plt.colorbar()
plt.gcf()
plt.savefig('porosidad_4.png')
#plt.show()
#%%
#print 'PC will shut down'
#os.system('sudo shutdown -P +2')        
# %%driver=gdal.GetDriverByName('GTiff')

'''
if os.path.exists('cota.tif'):
   driver.Delete('cota.tif')
salida=driver.Create('cota.tif',cot_arr_2.shape[1],cot_arr_2.shape[0],1,GDT_Float32)
salida.SetGeoTransform((0, 1, 0, 1000, 0, -1))
banda1=salida.GetRasterBand(1)
banda1.WriteArray(cot_arr_2)
salidaSRS = osr.SpatialReference()
salidaSRS.ImportFromEPSG(32618)
salida.SetProjection(salidaSRS.ExportToWkt())

if os.path.exists('profundidad.tif'):
   driver.Delete('profundidad.tif')
salida=driver.Create('profundidad.tif',prf_arr_2.shape[1],prf_arr_2.shape[0],1,GDT_Float32)
salida.SetGeoTransform((0, 1, 0, 1000, 0, -1))
banda1=salida.GetRasterBand(1)
banda1.WriteArray(prf_arr_2)
salidaSRS = osr.SpatialReference()
salidaSRS.ImportFromEPSG(32618)
salida.SetProjection(salidaSRS.ExportToWkt())


if os.path.exists('porosidad.tif'):
   driver.Delete('porosidad.tif')
salida=driver.Create('porosidad.tif',por_arr_2.shape[1],por_arr_2.shape[0],1,GDT_Float32)
salida.SetGeoTransform((0, 1, 0, 1000, 0, -1))
banda1=salida.GetRasterBand(1)
banda1.WriteArray(por_arr_2)
salidaSRS = osr.SpatialReference()
salidaSRS.ImportFromEPSG(32618)
salida.SetProjection(salidaSRS.ExportToWkt())

if os.path.exists('cota_4.tif'):
   driver.Delete('cota_4.tif')
salida=driver.Create('cota_4.tif',cot_arr_4.shape[1],cot_arr_4.shape[0],1,GDT_Float32)
salida.SetGeoTransform((0, 1, 0, 1000, 0, -1))
banda1=salida.GetRasterBand(1)
banda1.WriteArray(cot_arr_4)
salidaSRS = osr.SpatialReference()
salidaSRS.ImportFromEPSG(32618)
salida.SetProjection(salidaSRS.ExportToWkt())

if os.path.exists('profundidad_4.tif'):
   driver.Delete('profundidad_4.tif')
salida=driver.Create('profundidad_4.tif',prf_arr_4.shape[1],prf_arr_4.shape[0],1,GDT_Float32)
salida.SetGeoTransform((0, 1, 0, 1000, 0, -1))
banda1=salida.GetRasterBand(1)
banda1.WriteArray(prf_arr_4)
salidaSRS = osr.SpatialReference()
salidaSRS.ImportFromEPSG(32618)
salida.SetProjection(salidaSRS.ExportToWkt())


if os.path.exists('porosidad_4.tif'):
   driver.Delete('porosidad_4.tif')
salida=driver.Create('porosidad_4.tif',por_arr_4.shape[1],por_arr_4.shape[0],1,GDT_Float32)
salida.SetGeoTransform((0, 1, 0, 1000, 0, -1))
banda1=salida.GetRasterBand(1)
banda1.WriteArray(por_arr_4)
salidaSRS = osr.SpatialReference()
salidaSRS.ImportFromEPSG(32618)
salida.SetProjection(salidaSRS.ExportToWkt())

'''

print("It took me %s seconds." % (time.time() - start_Totaltime))

print 'Se ve que para exponentes mayores, la interpolación es más "borrosa" que en el caso con menor exponente, esto se puede deber a que se consideran con más "fuerza" las distintas contribuciones de los puntos existentes. No parece haber una razon lo suficientemente importante como para decidir que exponente utilizar. Se utilizaron 2 y 4, las imagenes producidas con el exponente 4 tienen sufijo _4'

#%%
def thick_calculation(cot, prf, por):
    cota_a_a=(200.+69.)*np.ones([1001, 1001])
    espesor=cot-prf-cota_a_a
    espesor[espesor<0]=0
    espesor_hc=espesor*por/100
    plt.figure(20)
    plt.imshow(espesor_hc)
    plt.colorbar()
    plt.savefig('espesor_hc.png')
    volumen=1.*1*espesor_hc #espesor por ancho en x y y de cada celda en metros
    print 'El volumen de hidrocarburo es ', sum(sum(volumen)), 'm**3'
    return sum(sum(volumen))

#plt.imshow(espesor)
#%%
print 'Con exponente 2'
thick_calculation(cot_arr_2, prf_arr_2, por_arr_2)
print 'Con exponente 4'
thick_calculation(cot_arr_4, prf_arr_4, por_arr_4)