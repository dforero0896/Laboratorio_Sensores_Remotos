#!/usr/bin/env python
import numpy as np
#import matplotlib.pyplot as plt
from osgeo import ogr, osr
import os

#Declaracion del formato en el que se guardara el archivo
formato = ogr.GetDriverByName("ESRI Shapefile")

#Creacion del archivo
if os.path.exists('Bogota.shp'):
   formato.DeleteDataSource('Bogota.shp')
archivo = formato.CreateDataSource("Bogota.shp")


#Especificacion del sistema de referencia que se va a utiliza en este caso wgs84
srs = osr.SpatialReference()
srs.ImportFromEPSG(4326)

#Creacion de la capa especificando que es un conjunto de lineas (ogr.wkbMultiLineString)
capa = archivo.CreateLayer("Bogota", srs, ogr.wkbPolygon)

#Declaracion de los atributos
nombre = ogr.FieldDefn("Nombre", ogr.OFTString)

#Tamano del atributo
nombre.SetWidth(24)

#Anadiendo el atributo a la capa
capa.CreateField(nombre)

region = ogr.FieldDefn("Region", ogr.OFTString)
region.SetWidth(24)
capa.CreateField(region)

poblacion = ogr.FieldDefn("Poblacion", ogr.OFTString)
poblacion.SetWidth(24)
capa.CreateField(poblacion)

alcalde = ogr.FieldDefn("Alcalde", ogr.OFTString)
alcalde.SetWidth(24)
capa.CreateField(alcalde)


region = ogr.FieldDefn("Region", ogr.OFTString)
region.SetWidth(24)

caracteristicas = ogr.Feature(capa.GetLayerDefn())

caracteristicas.SetField("Nombre", "Bogota")
caracteristicas.SetField("Region", "Cundinamarca")
caracteristicas.SetField("Poblacion", "8.081M")
caracteristicas.SetField("Alcalde", "Penalosa")

cuadro=ogr.Geometry(ogr.wkbLinearRing)
cuadro.AddPoint(-74.19726373334838,4.572470399422518,0)
cuadro.AddPoint(-74.16371505670787,4.556879831897574,0)
cuadro.AddPoint(-74.13006002225336,4.471213071426934,0)
cuadro.AddPoint(-74.09036073511163,4.506996316679183,0)
cuadro.AddPoint(-74.04713922667182,4.665808630413204,0)
cuadro.AddPoint(-74.02494390582396,4.685085320554879,0)
cuadro.AddPoint(-74.02878004098122,4.769788135089183,0)
cuadro.AddPoint(-74.05873480529803,4.775603398470346,0)
cuadro.AddPoint(-74.07758021138284,4.759226006604921,0)
cuadro.AddPoint(-74.11918680269677,4.757336492895785,0)
cuadro.AddPoint(-74.17094172021802,4.697578110822115,0)
cuadro.AddPoint(-74.16320292072183,4.663840317735374,0)
cuadro.AddPoint(-74.2106154763495,4.638760033645003,0)
cuadro.AddPoint(-74.20577657599677,4.603086378329431,0)
cuadro.AddPoint(-74.24258087097665,4.571225640929569,0)
cuadro.AddPoint(-74.19726373334838,4.572470399422518,0)
poly=ogr.Geometry(ogr.wkbPolygon)
poly.AddGeometry(cuadro)

#print poly.ExportToWkt()

ciudad = ogr.CreateGeometryFromWkt(poly.ExportToWkt())


#Insertando las vias a las caracteristicas
caracteristicas.SetGeometry(ciudad)

#Insertando las caracteristicas a la capa
capa.CreateFeature(caracteristicas)


'''
#Creacion del archivo
if os.path.exists('localidades.shp'):
   formato.DeleteDataSource('localidades.shp')
archivo = formato.CreateDataSource("localidades.shp")


caracteristicas1 = ogr.Feature(capa.GetLayerDefn())

caracteristicas1.SetField("Nombre", "ciudad1")
caracteristicas1.SetField("Region", "Cundinamarca1")


cuadro=ogr.Geometry(ogr.wkbLinearRing)
cuadro.AddPoint(-75,1)
cuadro.AddPoint(-72,2)
cuadro.AddPoint(-72,2)
cuadro.AddPoint(-75,1)
cuadro.AddPoint(-75,1)

poly=ogr.Geometry(ogr.wkbPolygon)
poly.AddGeometry(cuadro)

print poly.ExportToWkt()

#ciudad1 = ogr.CreateGeometryFromWkt(poly.ExportToWkt())


#Insertando las vias a las caracteristicas
#caracteristicas1.SetGeometry(ciudad1)

#Insertando las caracteristicas a la capa
#capa.CreateFeature(caracteristicas1)

'''
#'''
if os.path.exists('Bogota_proj.shp'):
   formato.DeleteDataSource('Bogota_proj.shp')
os.system('ogr2ogr -f "ESRI Shapefile" -t_srs EPSG:32618 Bogota_proj.shp Bogota.shp')
#'''

