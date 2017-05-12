#!/usr/bin/env python
import numpy as np
#import matplotlib.pyplot as plt
from osgeo import ogr, osr
import os

#Declaracion del formato en el que se guardara el archivo
formato = ogr.GetDriverByName("ESRI Shapefile")

#Creacion del archivo
if os.path.exists('parques.shp'):
   formato.DeleteDataSource('parques.shp')
archivo = formato.CreateDataSource("parques.shp")


#Especificacion del sistema de referencia que se va a utiliza en este caso wgs84
srs = osr.SpatialReference()
srs.ImportFromEPSG(4326)

#Creacion de la capa especificando que es un conjunto de lineas (ogr.wkbMultiLineString)
capa = archivo.CreateLayer("parques", srs, ogr.wkbPolygon)

#Declaracion de los atributos
nombre = ogr.FieldDefn("Nombre", ogr.OFTString)

#Tamano del atributo
nombre.SetWidth(24)

#Anadiendo el atributo a la capa
capa.CreateField(nombre)


caracteristicas = ogr.Feature(capa.GetLayerDefn())

caracteristicas.SetField("Nombre", "Simon Bolivar")

cuadro=ogr.Geometry(ogr.wkbLinearRing)
cuadro.AddPoint(-74.08872759580405,4.659276195789591,0)
cuadro.AddPoint(-74.09297581189871,4.665727152399576,0)
cuadro.AddPoint(-74.09480826188427,4.664386235894758,0)
cuadro.AddPoint(-74.10037148954892,4.657064916897975,0)
cuadro.AddPoint(-74.09348190016161,4.652325546123507,0)
cuadro.AddPoint(-74.09109388446676,4.653278870117076,0)
cuadro.AddPoint(-74.08872759580405,4.659276195789591,0)
poly=ogr.Geometry(ogr.wkbPolygon)
poly.AddGeometry(cuadro)

#print poly.ExportToWkt()

ciudad = ogr.CreateGeometryFromWkt(poly.ExportToWkt())


caracteristicas.SetGeometry(ciudad)


capa.CreateFeature(caracteristicas)




caracteristicas2 = ogr.Feature(capa.GetLayerDefn())

caracteristicas2.SetField("Nombre", "93")

cuadro2=ogr.Geometry(ogr.wkbLinearRing)
cuadro2.AddPoint(-74.04743595763337,4.676754248454302,0)
cuadro2.AddPoint(-74.04882898414213,4.677481743074504,0)
cuadro2.AddPoint(-74.04918668247359,4.676764009435455,0)
cuadro2.AddPoint(-74.04775404594979,4.676065008246718,0)
cuadro2.AddPoint(-74.04743595763337,4.676754248454302,0)
poly2=ogr.Geometry(ogr.wkbPolygon)
poly2.AddGeometry(cuadro2)

#print poly.ExportToWkt()

ciudad2 = ogr.CreateGeometryFromWkt(poly2.ExportToWkt())


caracteristicas2.SetGeometry(ciudad2)


capa.CreateFeature(caracteristicas2)




caracteristicas3 = ogr.Feature(capa.GetLayerDefn())

caracteristicas3.SetField("Nombre", "Virrey")

cuadro3=ogr.Geometry(ogr.wkbLinearRing)
cuadro3.AddPoint(-74.05383557422719,4.673335189054657,0)
cuadro3.AddPoint(-74.05865709316069,4.675893963601361,0)
cuadro3.AddPoint(-74.05873745357818,4.674772403565113,0)
cuadro3.AddPoint(-74.05417968226317,4.67256975080391,0)
cuadro3.AddPoint(-74.05383557422719,4.673335189054657,0)
poly3=ogr.Geometry(ogr.wkbPolygon)
poly3.AddGeometry(cuadro3)

#print poly.ExportToWkt()

ciudad3 = ogr.CreateGeometryFromWkt(poly3.ExportToWkt())


caracteristicas3.SetGeometry(ciudad3)


capa.CreateFeature(caracteristicas3)


