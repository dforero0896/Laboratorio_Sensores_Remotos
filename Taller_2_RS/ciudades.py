import ogr
import osr
import os

#Declaracion del formato en el que se guardara el archivo
formato = ogr.GetDriverByName("ESRI Shapefile")

#Creacion del archivo
if os.path.exists('ciudad3.shp'):
   formato.DeleteDataSource('ciudad3.shp')
archivo = formato.CreateDataSource("ciudad3.shp")


#Especificacion del sistema de referencia que se va a utiliza en este caso wgs84
srs = osr.SpatialReference()
srs.ImportFromEPSG(4326)

#Creacion de la capa especificando que es un conjunto de lineas (ogr.wkbMultiLineString)
capa = archivo.CreateLayer("ciudad", srs, ogr.wkbPolygon)

#Declaracion de los atributos
nombre = ogr.FieldDefn("Nombre", ogr.OFTString)

#Tamano del atributo
nombre.SetWidth(24)

#Anadiendo el atributo a la capa
capa.CreateField(nombre)

region = ogr.FieldDefn("Region", ogr.OFTString)
region.SetWidth(24)
capa.CreateField(region)

caracteristicas = ogr.Feature(capa.GetLayerDefn())

caracteristicas.SetField("Nombre", "ciudad")
caracteristicas.SetField("Region", "Cundinamarca")

'''
cuadro=ogr.Geometry(ogr.wkbLinearRing)
cuadro.AddPoint(-77,1)
cuadro.AddPoint(-77,2)
cuadro.AddPoint(-76,2)
cuadro.AddPoint(-76,1)
cuadro.AddPoint(-77,1)

poly=ogr.Geometry(ogr.wkbPolygon)
poly.AddGeometry(cuadro)

print poly.ExportToWkt()
'''
ciudad = ogr.CreateGeometryFromWkt('POLYGON ((-78 1, -78 2, -77 2 ,-77 1, -78 1))')


#Insertando las vias a las caracteristicas
caracteristicas.SetGeometry(ciudad)

#Insertando las caracteristicas a la capa
capa.CreateFeature(caracteristicas)


caracteristicas1 = ogr.Feature(capa.GetLayerDefn())

caracteristicas1.SetField("Nombre", "ciudad1")
caracteristicas1.SetField("Region", "Cundinamarca1")

'''
cuadro=ogr.Geometry(ogr.wkbLinearRing)
cuadro.AddPoint(-75,1)
cuadro.AddPoint(-72,2)
cuadro.AddPoint(-72,2)
cuadro.AddPoint(-75,1)
cuadro.AddPoint(-75,1)

poly=ogr.Geometry(ogr.wkbPolygon)
poly.AddGeometry(cuadro)

print poly.ExportToWkt()
'''
ciudad1 = ogr.CreateGeometryFromWkt('POLYGON ((-75 1, -75 2, -72 2 ,-72 1, -75 1))')


#Insertando las vias a las caracteristicas
caracteristicas1.SetGeometry(ciudad1)

#Insertando las caracteristicas a la capa
capa.CreateFeature(caracteristicas1)



