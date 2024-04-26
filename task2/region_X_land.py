# Create a shapefile for all the geography region elevation points on the Land
# and print how many point in each shape file

import arcpy

arcpy.env.overwriteOutput= True

region_points = r"C:\Users\zidan\Desktop\GISProj\Data\ne_10m_geography_regions_points.shp"
land = r"C:\Users\zidan\Desktop\GISProj\Data\ne_10m_land.shp"
output =r"C:\Users\zidan\Desktop\GISProj\Output\Task2"

# making layers
arcpy.MakeFeatureLayer_management(land, 'land')
arcpy.MakeFeatureLayer_management(region_points, 'reg_points')
# select relative points
arcpy.SelectLayerByLocation_management('reg_points', 'WITHIN', 'land')
# export .shp files
arcpy.FeatureClassToFeatureClass_conversion('ele_points', output, 'region_X_land')

taskOutput = output + r"\region_X_land.shp"
# count points
elements = arcpy.SearchCursor(taskOutput)
cntr = 0
for i in elements:
    cntr = cntr + 1
print(cntr)
