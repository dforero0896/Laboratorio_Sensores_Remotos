import numpy as np
import gdal
import os
import osr
from gdalconst import *
from mpi4py import MPI
import matplotlib.pyplot as plt
from collections import Counter
nortes,estes,cotas,profundidad,porosidad=np.loadtxt('PuntosTaller4.csv',dtype={'names':('norte','este','cota','profundidad','porosidad'),'formats':('f4','f4','f4','f4','f2')},delimiter=';',usecols=(0,1,2,3,4),unpack=True,skiprows=1)
grillaCota=np.empty((1001,1001))
grillaCota[:]=np.nan
for k in range(len(nortes)):
    x=estes[k]
    y=1000-nortes[k]
    grillaCota[y,x]=cotas[k]



grillaProf=np.empty((1001,1001))
grillaProf[:]=np.nan
for k in range(len(nortes)):
    x=estes[k]
    y=1000-nortes[k]
    grillaProf[y,x]=profundidad[k]




grillaPor=np.empty((1001,1001))
grillaPor[:]=np.nan
for k in range(len(nortes)):
    x=estes[k]
    y=1000-nortes[k]
    grillaPor[y,x]=porosidad[k]

#%%
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
print  rank, size

for i in range(size):
    print 'I am processor ',rank, ' of ', size 
#%%

plt.imshow(grillaCota)
#plt.show()

#%%
def h(x1, x2, y1, y2):
    return np.sqrt((x1-x2)**2+(y1-y2)**2)
    
from scipy.optimize import curve_fit
def func(x, a, b, c):
    return a * x + c




    
def semi(z):
    global func
    h_array=[]
    z_diff_sq=[]
    for i in range(len(nortes)):
        for k in range(i+1,len(nortes)):
            h_array.append(np.round(h(nortes[k], nortes[i], estes[k], estes[i])))
            z_diff_sq.append((z[i]-z[k])**2)
            rep_arr=Counter(h_array)
    z_diff_sq=np.array(z_diff_sq)
        
    data_arr_h=[]
    for i in range(len(h_array)):
        suma=sum(z_diff_sq[h_array==h_array[i]])
        data_arr_h.append(0.5*(rep_arr[h_array[i]])*suma)
    popt, pcov = curve_fit(func, h_array/np.mean(h_array), data_arr_h/np.mean(data_arr_h))
    xdata=np.linspace(min(h_array), max(h_array), 100)
    plt.plot(xdata, np.mean(data_arr_h)*func(xdata/np.mean(h_array), *popt), 'r-', label='fit')    
    plt.scatter(h_array, data_arr_h)
#    plt.show()
    return 0
#%%
#Para las cotas
plt.figure(1)
semi(cotas)
#%%
#Para profundidad
plt.figure(2)
semi(profundidad)
#%%
#Para porosidad
plt.figure(3)
semi(porosidad)

#%%

#%%    
n=2
def idwinterp(z, n):
    
    for i in range(1001):
        este=i
        for j in range(1001):
            norte=1000-j
            totalInvDistancia=0
            if np.isnan(z[j,i]):
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
if rank==0:
    plt.figure(4)
    idwinterp(grillaCota, 2)
    plt.gcf()
    plt.savefig('cota.png')
#plt.show()


#%%
    plt.figure(5)
    idwinterp(grillaProf, 2)
    plt.gcf()
    plt.savefig('profundidad.png')
#plt.show()
#%%
if rank==1:
    plt.figure(6)
    idwinterp(grillaPor, 2)
    plt.gcf()
    plt.savefig('porosidad.png')
#plt.show()
#%%
    plt.figure(7)
    idwinterp(grillaCota, 4)
    plt.gcf()
    plt.savefig('cota_4.png')
#plt.show()
#%%
if rank==2:
    plt.figure(8)
    idwinterp(grillaProf, 4)
    plt.gcf()
    plt.savefig('profundidad_4.png')
#plt.show()
#%%

    plt.figure(9)
    idwinterp(grillaPor, 4)
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
salida=driver.Create('cota.tif',grillaCota.shape[1],grillaCota.shape[0],1,GDT_Float32)
salida.SetGeoTransform((0, 1, 0, 1000, 0, -1))
banda1=salida.GetRasterBand(1)
banda1.WriteArray(grillaCota)
salidaSRS = osr.SpatialReference()
salidaSRS.ImportFromEPSG(32618)
salida.SetProjection(salidaSRS.ExportToWkt())
'''
