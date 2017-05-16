import time
start_time = time.time()
import numpy as np
import gdal
import os
import osr
from gdalconst import *
import matplotlib.pyplot as plt
from collections import Counter
nortes,estes,cotas,profundidad,porosidad=np.loadtxt('PuntosTaller4.csv',dtype={'names':('norte','este','cota','profundidad','porosidad'),'formats':('f4','f4','f4','f4','f2')},delimiter=';',usecols=(0,1,2,3,4),unpack=True,skiprows=1)


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
    plt.xlabel('h')
    plt.ylabel('$\gamma$')
#    plt.show()
    return 0
#%%
#Para las cotas
plt.figure(1)
semi(cotas)
plt.gcf()
plt.savefig('semivar_cotas.png')
#%%
#Para profundidad
plt.figure(2)
semi(profundidad)
plt.savefig('semivar_prof.png')
#%%
#Para porosidad
plt.figure(3)
semi(porosidad)
plt.savefig('semivar_por.png')


print("It took me %s seconds." % (time.time() - start_time))

