#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from osgeo import ogr, osr
import os

driver=ogr.GetDriverByName('ESRI Shapefile')
print type(driver)
srs=osr.SpatialReference()
print type(srs)

srs.ImportFromEPSG(4326)
print 'hola'
type(driver.CreateDataSource("Bogota.shp"))

