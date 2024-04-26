import arcpy

arcpy.env.overwriteOutput = True

Data = r"C:\Users\zidan\Desktop\GISProj\Data"
arcpy.env.workspace = Data

output = r"C:\Users\zidan\Desktop\GISProj\Output\task10"
ele_points = r"C:\Users\zidan\Desktop\GISProj\Data\ne_10m_geography_regions_elevation_points.shp"

featureclasses = set()
cursor = arcpy.SearchCursor(ele_points, ['featurecla'])
for i in cursor:
    featureclasses.add(i.getValue('featurecla'))


for i in featureclasses:
    arcpy.MakeFeatureLayer_management(ele_points, 'ele_points', """ "featurecla"='{}' AND "elevation">1500 AND "region" = 'Africa' """.format(i))
    arcpy.FeatureClassToFeatureClass_conversion('ele_points', output, 'ele_points_in_{}'.format(i))