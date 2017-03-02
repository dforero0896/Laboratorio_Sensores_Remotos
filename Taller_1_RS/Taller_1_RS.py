
# coding: utf-8



from osgeo import gdal
import numpy as np
#import matplotlib.pyplot as plt
import os
import subprocess
#import matplotlib.image as mpimg
from osgeo import gdal_array



# open raster and choose band to find min, max
raster = r'srtm_39_05.tif'
gtif = gdal.Open(raster)
srcband = gtif.GetRasterBand(1)
#datos = srcband.ReadAsArray()
print "Punto 1"
stats = srcband.GetStatistics(True, True)
print 'Min=', stats[0]
print 'Max=', stats[1]
print 'Mean=', stats[2]



os.system('gdal_translate -srcwin 0 0 1500 1500 srtm_39_05.tif cut.tif')



raster = r'cut.tif'
gtif_cut = gdal.Open(raster)
srcband_cut = gtif_cut.GetRasterBand(1)

traza=0
initial_DEM_arr=gtif_cut.ReadAsArray()
for i in range(0, 1500):
    value=initial_DEM_arr[i,i]
    #value=subprocess.check_output('gdallocationinfo cut.tif %d %d | grep Value | sed "s/^.*:\s//g"'%(i,i), shell=True)
    value=int(value)
    traza+=value    
print 'La suma de los elementos de la diagonal es ',traza

mypic = gdal.Open(r'mypic.jpg')
myband_1=mypic.GetRasterBand(1)
myband_2=mypic.GetRasterBand(2)
myband_3=mypic.GetRasterBand(3)

stats_R=myband_1.GetStatistics(True, True)
print 'Min R=', stats_R[0]
print 'Max R=', stats_R[1]
print 'Mean R= ', stats_R[2]
stats_G=myband_2.GetStatistics(True, True)
print 'Min G=', stats_G[0]
print 'Max G=', stats_G[1]
print 'Mean G= ', stats_G[2]
stats_B=myband_3.GetStatistics(True, True)
print 'Min B=', stats_B[0]
print 'Max B=', stats_B[1]
print 'Mean B= ', stats_B[2]

mypic_R=myband_1.ReadAsArray()
mypic_G=myband_2.ReadAsArray()
mypic_B=myband_3.ReadAsArray()
mypic_arr_tiff=mypic_R+mypic_G+mypic_B
from osgeo.gdalconst import *

driver = gtif.GetDriver()
mypic_out=driver.Create('mypic.tiff' , len(mypic_arr_tiff[0,:]), len(mypic_arr_tiff[:,0]), 1, GDT_Int32)
mypic_Band = mypic_out.GetRasterBand(1)
mypic_Band.WriteArray(mypic_arr_tiff, 0, 0)



os.system('gdal_translate -srcwin 299 0 10 10 mypic.tiff mycut.tiff')

littleCorner=gdal.Open(r'mycut.tiff')
littleBand=littleCorner.GetRasterBand(1)
littleStats= littleBand.GetStatistics(True, True)
print 'El valor promedio de la region de 10x10 es ', littleStats[2]

print 'El valor minimo de la region de 10x10 es ', littleStats[0]

print 'El valor maximo de la region de 10x10 es ', littleStats[1]




cut_arr=srcband_cut.ReadAsArray()

cut_arr[-1-len(mypic_arr_tiff[:,0]):-1,-1-len(mypic_arr_tiff[0,:]):-1 ]-=mypic_arr_tiff



driver = gtif.GetDriver()
DEM_mypic_out=driver.Create("DEM_mypic.tiff" , np.shape(cut_arr)[0], np.shape(cut_arr)[1], 1, GDT_Int32)
DEM_mypic_Band = DEM_mypic_out.GetRasterBand(1)
DEM_mypic_Band.WriteArray(cut_arr, 0, 0)






os.system("gdal_translate -outsize 60 60 cut.tif small_cut.tif")

small_cut=gdal.Open('small_cut.tif')
small_cut_band=small_cut.GetRasterBand(1)
small_cut_arr=small_cut_band.ReadAsArray()

mypic_Dem_arr=np.copy(mypic_arr_tiff).astype(np.int16)

mypic_Dem_arr[-1-len(small_cut_arr[:,0]):-1,:len(small_cut_arr[0,:])]+=small_cut_arr.astype(np.int16)

driver = gtif.GetDriver()
mypic_DEM_out=driver.Create('mypic_DEM.tif' , np.shape(cut_arr)[0], np.shape(cut_arr)[1], 1, GDT_Int32)
mypic_DEM_Band = mypic_DEM_out.GetRasterBand(1)
mypic_DEM_Band.WriteArray(mypic_Dem_arr, 0, 0)

os.system("gdal_translate -a_ullr 9.9995836 40.0004168 11.2495836 38.7504168 DEM_mypic.tiff DEM_mypic_geor.tiff")
os.system("gdalwarp -t_srs EPSG:23032 DEM_mypic_geor.tiff projected.tiff")

print 'LOS ERRORES QUE DA GDAL TRANSLATE AL PARECER SON BUGS EN WINDOWS, CUANDO CORRO LOS MISMOS COMANDOS FUERA DEL SCRIPT, FUNCIONA PERFECTO'

'''
from osgeo import osr

driver = gtif.GetDriver()

DEM_mypic_proj=driver.Create('DEM_mypic_proj.tiff' , np.shape(cut_arr)[0], np.shape(cut_arr)[1], 1, GDT_Int32)



proj=osr.SpatialReference()
#proj.SetWellKnownGeogCS("EPSG:4816")
proj.SetWellKnownGeogCS("EPSG:23032")
DEM_mypic_proj.SetProjection(proj.ExportToWkt())
geotransform=(1,0.1,0,40,0,0.1)

DEM_mypic_proj.SetGeoTransform(geotransform)

DEM_mypic_proj_Band = DEM_mypic_proj.GetRasterBand(1)
DEM_mypic_proj_Band.WriteArray(cut_arr, 0, 0)

'''

upperLeft=[9.9995836, 40.0004168]
lowerRight=[11.2495836, 38.7504168]

px=1500
Nx=(1500./(lowerRight[0]-upperLeft[0]))**-1
Ny=(1500./(lowerRight[1]-upperLeft[1]))**-1

print np.shape(cut_arr)

def getCoords(i, j):
	x=upperLeft[0] + np.floor(i*Nx)
	y=upperLeft[1] + np.floor(j*Ny)
	return np.array([x, y])

def function(x, y):
	return np.sin(x*np.sqrt(y))**1./3

function_pic = np.zeros(np.shape(cut_arr))

for i in range(1,np.shape(cut_arr)[-1]):
	for j in range(1,np.shape(cut_arr)[-1]):
		this=getCoords(i,j)
		function_pic[i,j]=function(this[0], this[1])


hmax=mypic_Band.GetStatistics(True, True)[1]
fmax=max(mypic_arr_tiff.max(axis=1))

function_pic *= (hmax/fmax)

resta_final=cut_arr-function_pic



driver = gtif.GetDriver()
restafinal=driver.Create('restafinal.tif' , np.shape(cut_arr)[0], np.shape(cut_arr)[1], 1, GDT_Int32)
restafinalBand = restafinal.GetRasterBand(1)
restafinalBand.WriteArray(resta_final, 0, 0)


print 'F*****g DONE'


