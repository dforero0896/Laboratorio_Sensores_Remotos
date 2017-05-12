#!/usr/bin/env python
import numpy as np
#import matplotlib.pyplot as plt
from osgeo import ogr, osr
import os

#Declaracion del formato en el que se guardara el archivo
formato = ogr.GetDriverByName("ESRI Shapefile")

#Creacion del archivo
if os.path.exists('localidades.shp'):
   formato.DeleteDataSource('localidades.shp')
archivo = formato.CreateDataSource("localidades.shp")


#Especificacion del sistema de referencia que se va a utiliza en este caso wgs84
srs = osr.SpatialReference()
srs.ImportFromEPSG(4326)

#Creacion de la capa especificando que es un conjunto de lineas (ogr.wkbMultiLineString)
capa = archivo.CreateLayer("localidades", srs, ogr.wkbPolygon)

#Declaracion de los atributos
nombre = ogr.FieldDefn("Nombre", ogr.OFTString)

#Tamano del atributo
nombre.SetWidth(24)

#Anadiendo el atributo a la capa
capa.CreateField(nombre)


caracteristicas = ogr.Feature(capa.GetLayerDefn())

caracteristicas.SetField("Nombre", "Engativa")

cuadro=ogr.Geometry(ogr.wkbLinearRing)
cuadro.AddPoint(-74.14985433384466,4.714887962426573,0)
cuadro.AddPoint(-74.13927827135656,4.7084346578581,0)
cuadro.AddPoint(-74.122015759969,4.695341478824926,0)
cuadro.AddPoint(-74.11938291327876,4.680976006437263,0)
cuadro.AddPoint(-74.10283728806009,4.655415396628772,0)
cuadro.AddPoint(-74.0804456724963,4.673412224635418,0)
cuadro.AddPoint(-74.08150606090054,4.676543797904877,0)
cuadro.AddPoint(-74.08395645323256,4.68601601634828,0)
cuadro.AddPoint(-74.09144402427471,4.698308458019165,0)
cuadro.AddPoint(-74.09369764552099,4.707162326762582,0)
cuadro.AddPoint(-74.09684949868382,4.713595731598283,0)
cuadro.AddPoint(-74.1021263349945,4.720679163906153,0)
cuadro.AddPoint(-74.11056315064644,4.729769432907599,0)
cuadro.AddPoint(-74.11981514589422,4.737290124253826,0)
cuadro.AddPoint(-74.12978231040312,4.735611783043236,0)
cuadro.AddPoint(-74.14769164766025,4.7273975201579,0)
cuadro.AddPoint(-74.15667027419245,4.719115822191366,0)
cuadro.AddPoint(-74.15694985037946,4.71763972769206,0)
cuadro.AddPoint(-74.15698980104646,4.717428896887958,0)
cuadro.AddPoint(-74.15212703442037,4.712987122668486,0)
cuadro.AddPoint(-74.14985433384466,4.714887962426573,0)
poly=ogr.Geometry(ogr.wkbPolygon)
poly.AddGeometry(cuadro)

#print poly.ExportToWkt()

ciudad = ogr.CreateGeometryFromWkt(poly.ExportToWkt())

caracteristicas1 = ogr.Feature(capa.GetLayerDefn())

caracteristicas1.SetField("Nombre", "Fontibon")


cuadro1=ogr.Geometry(ogr.wkbLinearRing)
cuadro1.AddPoint(-74.15516374802367,4.665253553903824,0)
cuadro1.AddPoint(-74.14564806370895,4.663551364631227,0)
cuadro1.AddPoint(-74.1400801942761,4.661699006726156,0)
cuadro1.AddPoint(-74.13450658294393,4.652984090108812,0)
cuadro1.AddPoint(-74.13441072808057,4.652671129570898,0)
cuadro1.AddPoint(-74.12824105951499,4.641617570063692,0)
cuadro1.AddPoint(-74.11579609334108,4.642265022394156,0)
cuadro1.AddPoint(-74.10338197509958,4.646230444941625,0)
cuadro1.AddPoint(-74.10414355576538,4.65096767933149,0)
cuadro1.AddPoint(-74.10865622768527,4.65670486442923,0)
cuadro1.AddPoint(-74.11092072563497,4.66268476132669,0)
cuadro1.AddPoint(-74.11677370420406,4.673465089265123,0)
cuadro1.AddPoint(-74.12223298799701,4.680610788318222,0)
cuadro1.AddPoint(-74.1213673901335,4.686776064828877,0)
cuadro1.AddPoint(-74.12232501292937,4.690769818189081,0)
cuadro1.AddPoint(-74.12555364970658,4.694378462867963,0)
cuadro1.AddPoint(-74.13364356599892,4.701151168561867,0)
cuadro1.AddPoint(-74.14646285822818,4.710261252819556,0)
cuadro1.AddPoint(-74.14672590300255,4.710430249921908,0)
cuadro1.AddPoint(-74.15445230531691,4.712869382879857,0)
cuadro1.AddPoint(-74.16921130958073,4.703592435964154,0)
cuadro1.AddPoint(-74.17321098452524,4.69657174613312,0)
cuadro1.AddPoint(-74.16892940427097,4.688724996457124,0)
cuadro1.AddPoint(-74.17417667627939,4.67597319844571,0)
cuadro1.AddPoint(-74.17411804203726,4.675540609270195,0)
cuadro1.AddPoint(-74.17405938269069,4.675107887140666,0)
cuadro1.AddPoint(-74.16089129590456,4.665225925334066,0)
cuadro1.AddPoint(-74.15516374802367,4.665253553903824,0)
poly1=ogr.Geometry(ogr.wkbPolygon)
poly1.AddGeometry(cuadro1)

#print poly2.ExportToWkt()

ciudad1 = ogr.CreateGeometryFromWkt(poly1.ExportToWkt())

caracteristicas2 = ogr.Feature(capa.GetLayerDefn())

caracteristicas2.SetField("Nombre", "Kennedy")


cuadro2=ogr.Geometry(ogr.wkbLinearRing)
cuadro2.AddPoint(-74.1363719580223,4.651202924399649,0)
cuadro2.AddPoint(-74.14309697825343,4.659611058939528,0)
cuadro2.AddPoint(-74.14904034327432,4.65990547585728,0)
cuadro2.AddPoint(-74.15540774545212,4.659972581508487,0)
cuadro2.AddPoint(-74.15586039212388,4.660030199756885,0)
cuadro2.AddPoint(-74.16052906779238,4.657487205957478,0)
cuadro2.AddPoint(-74.16910633656244,4.653805007219584,0)
cuadro2.AddPoint(-74.17927968186403,4.651998637523477,0)
cuadro2.AddPoint(-74.18602690783057,4.647321093070061,0)
cuadro2.AddPoint(-74.19932034578223,4.645274793221358,0)
cuadro2.AddPoint(-74.20632066927406,4.637997942163132,0)
cuadro2.AddPoint(-74.20642488135323,4.637450067437714,0)
cuadro2.AddPoint(-74.20774387883976,4.629024508157917,0)
cuadro2.AddPoint(-74.20798333802512,4.628499350846509,0)
cuadro2.AddPoint(-74.2081397525408,4.627677647310525,0)
cuadro2.AddPoint(-74.20524323698103,4.62077634019832,0)
cuadro2.AddPoint(-74.19828280470851,4.618523843326536,0)
cuadro2.AddPoint(-74.19184903331487,4.615915820114116,0)
cuadro2.AddPoint(-74.18299487233749,4.619275825925065,0)
cuadro2.AddPoint(-74.17797271517355,4.611182255680623,0)
cuadro2.AddPoint(-74.17592772136788,4.607702627621711,0)
cuadro2.AddPoint(-74.15519418565133,4.600326575901547,0)
cuadro2.AddPoint(-74.14480604409621,4.601092016764705,0)
cuadro2.AddPoint(-74.13932204777919,4.615406375235881,0)
cuadro2.AddPoint(-74.13662522436491,4.62871865325811,0)
cuadro2.AddPoint(-74.12895701122892,4.63965182789418,0)
cuadro2.AddPoint(-74.1363719580223,4.651202924399649,0)
poly2=ogr.Geometry(ogr.wkbPolygon)
poly2.AddGeometry(cuadro2)

#print poly1.ExportToWkt()

ciudad2 = ogr.CreateGeometryFromWkt(poly2.ExportToWkt())



caracteristicas3 = ogr.Feature(capa.GetLayerDefn())

caracteristicas3.SetField("Nombre", "Suba")


cuadro3=ogr.Geometry(ogr.wkbLinearRing)
cuadro3.AddPoint(-74.07027684385633,4.759111692821433,0)
cuadro3.AddPoint(-74.07575499966232,4.758758124607788,0)
cuadro3.AddPoint(-74.09349555744417,4.760434948356214,0)
cuadro3.AddPoint(-74.11338090025228,4.75874616407281,0)
cuadro3.AddPoint(-74.12674634242498,4.746347409455045,0)
cuadro3.AddPoint(-74.12723333839618,4.745602335095402,0)
cuadro3.AddPoint(-74.12456247277424,4.738937797923349,0)
cuadro3.AddPoint(-74.1108229333155,4.735450735620606,0)
cuadro3.AddPoint(-74.10257563791564,4.726363717957348,0)
cuadro3.AddPoint(-74.10168545767245,4.726364808541157,0)
cuadro3.AddPoint(-74.09300850082664,4.717224286318734,0)
cuadro3.AddPoint(-74.08887358253779,4.708397837427541,0)
cuadro3.AddPoint(-74.08678517692663,4.695727775301866,0)
cuadro3.AddPoint(-74.074277375856,4.678469467352366,0)
cuadro3.AddPoint(-74.06063591319776,4.668217506275373,0)
cuadro3.AddPoint(-74.05842678678405,4.68333573843146,0)
cuadro3.AddPoint(-74.04578664880944,4.752669473229423,0)
cuadro3.AddPoint(-74.04577806818865,4.751918448474233,0)
cuadro3.AddPoint(-74.07027684385633,4.759111692821433,0)
poly3=ogr.Geometry(ogr.wkbPolygon)
poly3.AddGeometry(cuadro3)

#print poly1.ExportToWkt()

ciudad3 = ogr.CreateGeometryFromWkt(poly3.ExportToWkt())



caracteristicas4 = ogr.Feature(capa.GetLayerDefn())

caracteristicas4.SetField("Nombre", "Usaquen")


cuadro4=ogr.Geometry(ogr.wkbLinearRing)
cuadro4.AddPoint(-74.04098283980876,4.679125326094791,0)
cuadro4.AddPoint(-74.0286813728071,4.683095792233645,0)
cuadro4.AddPoint(-74.02773331140951,4.683635763418007,0)
cuadro4.AddPoint(-74.02759995255759,4.683770657365954,0)
cuadro4.AddPoint(-74.02824536067827,4.708798372860151,0)
cuadro4.AddPoint(-74.02824074993781,4.709084493248925,0)
cuadro4.AddPoint(-74.02808737905431,4.709801578004732,0)
cuadro4.AddPoint(-74.02218258420044,4.733536991860215,0)
cuadro4.AddPoint(-74.02677052940435,4.743964821169654,0)
cuadro4.AddPoint(-74.03772258228666,4.748385356322955,0)
cuadro4.AddPoint(-74.03801327210161,4.748384233314619,0)
cuadro4.AddPoint(-74.03873743427116,4.748684592937689,0)
cuadro4.AddPoint(-74.04600217443669,4.748378811062964,0)
cuadro4.AddPoint(-74.0464487089983,4.744750819864533,0)
cuadro4.AddPoint(-74.04936052658391,4.729971589668618,0)
cuadro4.AddPoint(-74.05122158781349,4.721900881863124,0)
cuadro4.AddPoint(-74.05291654727446,4.711468554768368,0)
cuadro4.AddPoint(-74.05472791973881,4.701326543402193,0)
cuadro4.AddPoint(-74.05813230487625,4.681054582098869,0)
cuadro4.AddPoint(-74.05859072336078,4.665124912165866,0)
cuadro4.AddPoint(-74.04698283990943,4.662488027132098,0)
cuadro4.AddPoint(-74.04644162292544,4.662496028560618,0)
cuadro4.AddPoint(-74.04098283980876,4.679125326094791,0)
poly4=ogr.Geometry(ogr.wkbPolygon)
poly4.AddGeometry(cuadro4)

#print poly1.ExportToWkt()

ciudad4 = ogr.CreateGeometryFromWkt(poly4.ExportToWkt())

#Insertando las vias a las caracteristicas
caracteristicas.SetGeometry(ciudad)
caracteristicas1.SetGeometry(ciudad1)
caracteristicas2.SetGeometry(ciudad2)
caracteristicas3.SetGeometry(ciudad3)
caracteristicas4.SetGeometry(ciudad4)




#Insertando las caracteristicas a la capa
capa.CreateFeature(caracteristicas)
capa.CreateFeature(caracteristicas1)
capa.CreateFeature(caracteristicas2)
capa.CreateFeature(caracteristicas3)
capa.CreateFeature(caracteristicas4)





'''
#Creacion del archivo
if os.path.exists('localidades.shp'):
   formato.DeleteDataSource('localidades.shp')
archivo = formato.CreateDataSource("localidades.shp")


caracteristicas2 = ogr.Feature(capa.GetLayerDefn())

caracteristicas2.SetField("Nombre", "ciudad1")
caracteristicas2.SetField("Region", "Cundinamarca1")


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
#caracteristicas2.SetGeometry(ciudad1)

#Insertando las caracteristicas a la capa
#capa.CreateFeature(caracteristicas2)

'''
