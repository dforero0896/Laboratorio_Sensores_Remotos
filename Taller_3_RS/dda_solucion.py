import ogr
import gdal
from gdalconst import *
import osr
import os
import numpy as np
import math as mt
shapefile = "vias.shp" 
driver = ogr.GetDriverByName("ESRI Shapefile")
dataSource = driver.Open(shapefile, 1)
print type(dataSource)
capa = dataSource.GetLayer()


def getMinMax(capavia):
    minx=100000000000
    maxx=-1000000000
    miny=100000000000
    maxy=-100000000000
    features=[]
    for feature in capavia:
        geom = feature.GetGeometryRef()
        puntos=[]
        for i in range(len(geom.GetPoints())):
            puntos.append((geom.GetX(i),geom.GetY(i)))
            if minx > geom.GetX(i):
               minx=geom.GetX(i)
               y0=geom.GetY(i)
            if miny>geom.GetY(i):
               miny=geom.GetY(i)
            if maxy<geom.GetY(i):
               maxy=geom.GetY(i)
            if maxx<geom.GetX(i):
               maxx=geom.GetX(i)
        features.append(puntos)
    return minx,maxx,miny,maxy,y0,features

def dda(capavia):
    minx,maxx,miny,maxy,y0,features=getMinMax(capavia)
    res=0.000277777777777
    r=np.zeros((mt.ceil((maxy-miny)/res),mt.ceil((maxx-minx)/res)))
    print r.shape
    for feature in features:
        for i in range(len(feature)-1):
            x1=feature[i][0]
            y1=feature[i][1]
            x2=feature[i+1][0]
            y2=feature[i+1][1]
            if x1>x2:
                temp=x1
                x1=x2
                x2=temp
                temp=y1
                y1=y2
                y2=temp
            m=(y2-y1)/(x2-x1)
            x=int((x1-minx)/res)
            y=int((y1-miny)/res)
            xf=int((x2-minx)/res)
            yf=int((y2-miny)/res)
            r[y,x]=1
            if abs(m)<1:
               while(x<xf):
                 x=x+1
                 y=y+m
                 r[round(y),x]=1
            elif abs(m)>=1:
                if m>0:
                    while(y<yf):
                        x+=1./abs(m)
                        y+=1
                        if round(x)==588.:
                            print 'hola'
                            
                            x=587
                        r[round(y),round(x)]=1
                else:
                    while(y>yf):
                        x+=1./abs(m)
                        y-=1
                        if round(x)==588.:
                            x=587
                        r[round(y),round(x)]=1

             #   print round(y),round(x)   
                    
    return r,minx,miny,res
resultado,xdef,ydef,reso=dda(capa)
print 'voy bien'
driver=gdal.GetDriverByName('GTiff')
if os.path.exists('resultado.tif'):
   driver.Delete('resultado.tif')
salida=driver.Create('resultado.tif',resultado.shape[1],resultado.shape[0],1,GDT_Float32)
salida.SetGeoTransform((xdef, reso, 0, ydef, 0, reso))
banda1=salida.GetRasterBand(1)
banda1.WriteArray(resultado)
salidaSRS = osr.SpatialReference()
salidaSRS.ImportFromEPSG(4326)
salida.SetProjection(salidaSRS.ExportToWkt())
