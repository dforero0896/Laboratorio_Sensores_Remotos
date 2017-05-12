#!/usr/bin/env python
import numpy as np
#import matplotlib.pyplot as plt
from osgeo import ogr, osr
import os

#Declaracion del formato en el que se guardara el archivo
formato = ogr.GetDriverByName("ESRI Shapefile")

#Creacion del archivo
if os.path.exists('vias.shp'):
   formato.DeleteDataSource('vias.shp')
archivo = formato.CreateDataSource("vias.shp")


#Especificacion del sistema de referencia que se va a utiliza en este caso wgs84
srs = osr.SpatialReference()
srs.ImportFromEPSG(4326)
file = open('vias.prj', 'w')
file.write(srs.ExportToWkt())
file.close()

#Creacion de la capa especificando que es un conjunto de lineas (ogr.wkbMultiLineString)
capa = archivo.CreateLayer("vias", srs, ogr.wkbLineString)

#Declaracion de los atributos
nombre = ogr.FieldDefn("Nombre", ogr.OFTString)

#Tamano del atributo
nombre.SetWidth(24)

#Anadiendo el atributo a la capa
capa.CreateField(nombre)


caracteristicas = ogr.Feature(capa.GetLayerDefn())

caracteristicas.SetField("Nombre", "Septima")

cuadro=ogr.Geometry(ogr.wkbLineString)
cuadro.AddPoint(-74.10084981798808,4.568812098885992,0)
cuadro.AddPoint(-74.08920521078578,4.583156976744309,0)
cuadro.AddPoint(-74.07602096095482,4.603302564950458,0)
cuadro.AddPoint(-74.06878122531356,4.617063259104982,0)
cuadro.AddPoint(-74.04161797010977,4.674500951391213,0)
cuadro.AddPoint(-74.03524852363684,4.686444608883745,0)
cuadro.AddPoint(-74.03152458085108,4.69661423528704,0)
cuadro.AddPoint(-74.02883134017333,4.700016514344307,0)
cuadro.AddPoint(-74.02880125311873,4.715374094105969,0)
cuadro.AddPoint(-74.02871847540435,4.717276323527361,0)
cuadro.AddPoint(-74.02401901074749,4.729941616440942,0)
cuadro.AddPoint(-74.02418750897091,4.735987728646456,0)
cuadro.AddPoint(-74.02283866345957,4.7378464396636,0)
cuadro.AddPoint(-74.02415492075159,4.751343769945989,0)
cuadro.AddPoint(-74.02760161630388,4.767066644619928,0)
cuadro.AddPoint(-74.02608054844065,4.776107270750104,0)
poly=ogr.Geometry(ogr.wkbLineString)
poly.AddGeometry(cuadro)

#print poly.ExportToWkt()

ciudad = ogr.CreateGeometryFromWkt(cuadro.ExportToWkt())


caracteristicas.SetGeometry(ciudad)


capa.CreateFeature(caracteristicas)




caracteristicas2 = ogr.Feature(capa.GetLayerDefn())

caracteristicas2.SetField("Nombre", "Boyaca")

cuadro2=ogr.Geometry(ogr.wkbLineString)
cuadro2.AddPoint(-74.12029896050834,4.656683494135724,0) 
cuadro2.AddPoint(-74.11271100163341,4.665116830496347,0) 
cuadro2.AddPoint(-74.09050948727723,4.69456311175117,0) 
cuadro2.AddPoint(-74.08343749725155,4.697104380738367,0) 
cuadro2.AddPoint(-74.08104411415995,4.703251359890087,0) 
cuadro2.AddPoint(-74.08186197628268,4.706195093574913,0) 
cuadro2.AddPoint(-74.07632157475875,4.715630184175456,0) 
cuadro2.AddPoint(-74.06869507932348,4.729630386710529,0) 
cuadro2.AddPoint(-74.06639525258075,4.736374813563693,0) 
cuadro2.AddPoint(-74.06628697562769,4.7595140430681,0) 
cuadro2.AddPoint(-74.06573102043626,4.760324674634004,0) 
poly2=ogr.Geometry(ogr.wkbLineString)
poly2.AddGeometry(cuadro2)

#print poly.ExportToWkt()

ciudad2 = ogr.CreateGeometryFromWkt(cuadro2.ExportToWkt())


caracteristicas2.SetGeometry(ciudad2)


capa.CreateFeature(caracteristicas2)




caracteristicas3 = ogr.Feature(capa.GetLayerDefn())

caracteristicas3.SetField("Nombre", "Calle 26")

cuadro3=ogr.Geometry(ogr.wkbLineString)
cuadro3.AddPoint(-74.0703953389045,4.611583330152424,0)
cuadro3.AddPoint(-74.07316836841929,4.615880120802335,0)
cuadro3.AddPoint(-74.08000956697407,4.625744048149529,0)
cuadro3.AddPoint(-74.08189564463895,4.628302489464391,0)
cuadro3.AddPoint(-74.08440268517511,4.632100510942348,0)
cuadro3.AddPoint(-74.09074968281529,4.634710709115439,0)
cuadro3.AddPoint(-74.09175552959567,4.635504818825941,0)
cuadro3.AddPoint(-74.09505272141095,4.64049242860496,0)
cuadro3.AddPoint(-74.1062027854901,4.658040688141794,0)
cuadro3.AddPoint(-74.11626829055183,4.673637487415496,0)
cuadro3.AddPoint(-74.12240410167294,4.682930836678758,0)
cuadro3.AddPoint(-74.13190003504052,4.690118428053138,0)
cuadro3.AddPoint(-74.13753993692011,4.694230171611074,0)
cuadro3.AddPoint(-74.14181685545564,4.697801598890113,0)
poly3=ogr.Geometry(ogr.wkbLineString)
poly3.AddGeometry(cuadro3)

#print poly.ExportToWkt()

ciudad3 = ogr.CreateGeometryFromWkt(cuadro3.ExportToWkt())


caracteristicas3.SetGeometry(ciudad3)


capa.CreateFeature(caracteristicas3)



caracteristicas4 = ogr.Feature(capa.GetLayerDefn())

caracteristicas4.SetField("Nombre", "Autopista Norte")

cuadro4=ogr.Geometry(ogr.wkbLineString)
cuadro4.AddPoint(-74.03505361129804,4.822812730678726,0)
cuadro4.AddPoint(-74.04804720466329,4.741681979996661,0)
cuadro4.AddPoint(-74.06003177060735,4.670379399044723,0)
cuadro4.AddPoint(-74.06080040438241,4.665870329474043,0)
poly4=ogr.Geometry(ogr.wkbLineString)
poly4.AddGeometry(cuadro4)

#print poly.ExportToWkt()

ciudad4 = ogr.CreateGeometryFromWkt(cuadro4.ExportToWkt())


caracteristicas4.SetGeometry(ciudad4)


capa.CreateFeature(caracteristicas4)






caracteristicas5 = ogr.Feature(capa.GetLayerDefn())

caracteristicas5.SetField("Nombre", "NQS")

cuadro5=ogr.Geometry(ogr.wkbLineString)
cuadro5.AddPoint(-74.09776572944398,4.605953959570523,0)
cuadro5.AddPoint(-74.08399000512431,4.623312280993657,0)
cuadro5.AddPoint(-74.08085877401763,4.627053401589853,0)
cuadro5.AddPoint(-74.07797456133051,4.657807890541692,0)
cuadro5.AddPoint(-74.07602552211796,4.66439426876329,0)
cuadro5.AddPoint(-74.06004864659994,4.677722700068118,0)
cuadro5.AddPoint(-74.03670984550057,4.691383673473427,0)
cuadro5.AddPoint(-74.03315096366488,4.697470823869955,0)
cuadro5.AddPoint(-74.03176510231047,4.748022654805763,0)
poly5=ogr.Geometry(ogr.wkbLineString)
poly5.AddGeometry(cuadro5)

#print poly.ExportToWkt()

ciudad5 = ogr.CreateGeometryFromWkt(cuadro5.ExportToWkt())


caracteristicas5.SetGeometry(ciudad5)


capa.CreateFeature(caracteristicas5)



caracteristicas6 = ogr.Feature(capa.GetLayerDefn())

caracteristicas6.SetField("Nombre", "Calle 80")

cuadro6=ogr.Geometry(ogr.wkbLineString)
cuadro6.AddPoint(-74.12293925648784,4.724276522218538,0)
cuadro6.AddPoint(-74.113715644712,4.711778236204735,0)
cuadro6.AddPoint(-74.10873701588434,4.706854538073028,0)
cuadro6.AddPoint(-74.10103801454585,4.703012311758434,0)
cuadro6.AddPoint(-74.08854309300089,4.695129638218912,0)
cuadro6.AddPoint(-74.07906034736149,4.683766744036085,0)
cuadro6.AddPoint(-74.07505811564256,4.679165614515118,0)
cuadro6.AddPoint(-74.06799993040609,4.674287747655213,0)
cuadro6.AddPoint(-74.06149373787883,4.666205169244516,0)
poly6=ogr.Geometry(ogr.wkbLineString)
poly6.AddGeometry(cuadro6)

#print poly.ExportToWkt()

ciudad6 = ogr.CreateGeometryFromWkt(cuadro6.ExportToWkt())


caracteristicas6.SetGeometry(ciudad6)


capa.CreateFeature(caracteristicas6)








caracteristicas7 = ogr.Feature(capa.GetLayerDefn())

caracteristicas7.SetField("Nombre", "Americas")

cuadro7=ogr.Geometry(ogr.wkbLineString)
cuadro7.AddPoint(-74.0845152335897,4.624729057048534,0) 
cuadro7.AddPoint(-74.1335609517695,4.629932373080807,0) 
cuadro7.AddPoint(-74.14930239049515,4.632322354792388,0) 
poly7=ogr.Geometry(ogr.wkbLineString)
poly7.AddGeometry(cuadro7)

#print poly.ExportToWkt()

ciudad7 = ogr.CreateGeometryFromWkt(cuadro7.ExportToWkt())


caracteristicas7.SetGeometry(ciudad7)


capa.CreateFeature(caracteristicas7)







caracteristicas8 = ogr.Feature(capa.GetLayerDefn())

caracteristicas8.SetField("Nombre", "Cali")

cuadro8=ogr.Geometry(ogr.wkbLineString)
cuadro8.AddPoint(-74.18613354801116,4.618434675962488,0)
cuadro8.AddPoint(-74.18285330317318,4.619447287742177,0)
cuadro8.AddPoint(-74.17688073293449,4.626039414156474,0)
cuadro8.AddPoint(-74.17021996535749,4.628815470763137,0)
cuadro8.AddPoint(-74.14636482417481,4.64983403816759,0)
cuadro8.AddPoint(-74.13598543067717,4.659239840944532,0)
cuadro8.AddPoint(-74.11970739017255,4.679146221124564,0)
cuadro8.AddPoint(-74.10909351882576,4.689998092418822,0)
cuadro8.AddPoint(-74.10145900247166,4.702771378899208,0)
cuadro8.AddPoint(-74.09433814477691,4.7102488614542,0)
cuadro8.AddPoint(-74.09235053199672,4.716938998927239,0)
poly8=ogr.Geometry(ogr.wkbLineString)
poly8.AddGeometry(cuadro8)

#print poly.ExportToWkt()

ciudad8 = ogr.CreateGeometryFromWkt(cuadro8.ExportToWkt())


caracteristicas8.SetGeometry(ciudad8)


capa.CreateFeature(caracteristicas8)


if os.path.exists('Bogota-planas.shp'):
cuadro.AddPoint(-74.02883134017333,4.700016514344307,0)
   formato.DeleteDataSource('Bogota-planas.shp')
if os.path.exists('Bogota-coords.shp'):
   formato.DeleteDataSource('Bogota-coords.shp')
os.system('ogr2ogr -f "ESRI Shapefile" -a_srs EPSG:4326 Bogota-coords.shp Bogota.shp')

os.system('ogr2ogr -f "ESRI Shapefile" -t_srs EPSG:32618 Bogota-planas.shp Bogota-coords.shp')


if os.path.exists('localidades-planas.shp'):
   formato.DeleteDataSource('localidades-planas.shp')

if os.path.exists('localidades-coords.shp'):
   formato.DeleteDataSource('localidades-coords.shp')
os.system('ogr2ogr -f "ESRI Shapefile" -a_srs EPSG:4326 localidades-coords.shp localidades.shp')

os.system('ogr2ogr -f "ESRI Shapefile" -t_srs EPSG:32618 localidades-planas.shp localidades-coords.shp')


if os.path.exists('ccs-planas.shp'):
   formato.DeleteDataSource('ccs-planas.shp')
if os.path.exists('ccs-coords.shp'):
   formato.DeleteDataSource('ccs-coords.shp')
os.system('ogr2ogr -f "ESRI Shapefile" -a_srs EPSG:4326 ccs-coords.shp ccs.shp')

os.system('ogr2ogr -f "ESRI Shapefile" -t_srs EPSG:32618 ccs-planas.shp ccs-coords.shp')


if os.path.exists('parques-planas.shp'):
   formato.DeleteDataSource('parques-planas.shp')
if os.path.exists('parques-coords.shp'):
   formato.DeleteDataSource('parques-coords.shp')
os.system('ogr2ogr -f "ESRI Shapefile" -a_srs EPSG:4326 parques-coords.shp parques.shp')

os.system('ogr2ogr -f "ESRI Shapefile" -t_srs EPSG:32618 parques-planas.shp parques-coords.shp')

# Este no funciona aca, sacar del codigo directamente a la terminal
if os.path.exists('vias-planas.shp'):
   formato.DeleteDataSource('vias-planas.shp')

os.system('ogr2ogr -f "ESRI Shapefile" -t_srs EPSG:32618 vias-planas.shp vias.shp')
