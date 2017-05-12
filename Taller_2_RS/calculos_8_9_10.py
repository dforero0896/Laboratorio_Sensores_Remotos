from osgeo import ogr
import os
import numpy as np

shapefile = "Bogota-planas.shp"
driver = ogr.GetDriverByName("ESRI Shapefile")
dataSource = driver.Open(shapefile, 1)
capa = dataSource.GetLayer()

#poligonos=[]
for feature in capa:
    geom = feature.GetGeometryRef()
    poly = geom.ExportToWkt()
    #poligonos.append(poly)

#poly1=ogr.CreateGeometryFromWkt(poligonos[1])
#poly2=ogr.CreateGeometryFromWkt(poligonos[0])
import re
non_decimal = re.compile(r'[^\d.\,\d\s\d.]+')
#interseccion=poly1.Intersection(poly2)
polyArr=non_decimal.sub('', poly).split(',')[1:]

for i in range(len(polyArr)):
    polyArr[i]=np.array(polyArr[i].split(' '), dtype=float)


def calcDist(coords1, coords2):
    x1=coords1[0]
    y1=coords1[1]
    x2=coords2[0]
    y2=coords2[1]
    return np.sqrt((x2-x1)**2 + (y2-y1)**2)

perimetro=0

for i in range(len(polyArr)-1):
    perimetro+=calcDist(polyArr[i], polyArr[i+1])
print 'El perimetro de Bogota es: ', perimetro/1000, 'km'

area=polyArr[0][0]*polyArr[1][1]

for i in range(1,len(polyArr)-1):
    area+=polyArr[i][0]*(polyArr[i+1][1]-polyArr[i-1][1])

area-=polyArr[-1][0]*polyArr[-2][1]
area=abs(area)

print 'El area de Bogota es ', area/(1e3)**2, 'km^2'

shapefile = "vias-planas.shp"
driver = ogr.GetDriverByName("ESRI Shapefile")
dataSource = driver.Open(shapefile, 1)
capa = dataSource.GetLayer()
for feature in capa:

    geom = feature.GetGeometryRef()
    poly = geom.ExportToWkt()
    polyArr=non_decimal.sub('', poly).split(',')[1:]
    for i in range(len(polyArr)):
        polyArr[i]=np.array(polyArr[i].split(' '), dtype=float)
    lon=0
    for i in range(len(polyArr)-1):
        lon+=calcDist(polyArr[i], polyArr[i+1])
    print 'La longitud de la ', feature.GetFieldAsString(0),'es ', lon/1000, 'km'



shapefile = "localidades-planas.shp"
driver = ogr.GetDriverByName("ESRI Shapefile")
dataSource = driver.Open(shapefile, 1)
capa = dataSource.GetLayer()
for feature in capa:
    geom = feature.GetGeometryRef()
    poly = geom.ExportToWkt()
    polyArr=non_decimal.sub('', poly).split(',')[1:]
    for i in range(len(polyArr)):
        polyArr[i]=np.array(polyArr[i].split(' '), dtype=float)
        
    area=polyArr[0][0]*polyArr[1][1]
    for i in range(1,len(polyArr)-1):
        area+=polyArr[i][0]*(polyArr[i+1][1]-polyArr[i-1][1])
    area-=polyArr[-1][0]*polyArr[-2][1]
    area=abs(area)
    print 'El area de ', feature.GetFieldAsString(0),' es ', area/(1e3)**2, 'km^2'




shapefile = "parques-planas.shp"
driver = ogr.GetDriverByName("ESRI Shapefile")
dataSource = driver.Open(shapefile, 1)
capa = dataSource.GetLayer()
for feature in capa:
    geom = feature.GetGeometryRef()
    poly = geom.ExportToWkt()
    polyArr=non_decimal.sub('', poly).split(',')[1:]
    for i in range(len(polyArr)):
        polyArr[i]=np.array(polyArr[i].split(' '), dtype=float)
        
    area=polyArr[0][0]*polyArr[1][1]
    for i in range(1,len(polyArr)-1):
        area+=polyArr[i][0]*(polyArr[i+1][1]-polyArr[i-1][1])
    area-=polyArr[-1][0]*polyArr[-2][1]
    area=abs(area)

    print 'El area del parque ', feature.GetFieldAsString(0),' es ', area/(1e3)**2, 'km^2'
