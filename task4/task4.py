import arcpy

arcpy.env.overwriteOutput = True

Data = r"..\Data"
output = r"C:\Users\zidan\Desktop\GISProj\Output\task4"

elevation_region_points = r"C:\Users\zidan\Desktop\GISProj\Data\ne_10m_geography_regions_elevation_points.shp"
glaciated = r"C:\Users\zidan\Desktop\GISProj\Data\ne_10m_glaciated_areas.shp"



regions = set()

cursor = arcpy.SearchCursor(elevation_region_points, ['region'])
for i in cursor:
    regions.add(i.getValue('region'))

arcpy.MakeFeatureLayer_management(glaciated, 'glaciated')

for i in regions:
    print(i)
    arcpy.MakeFeatureLayer_management(elevation_region_points,  'points', """ "region"='{}' """.format(i))
    arcpy.SelectLayerByLocation_management('points', 'WITHIN', 'glaciated')
    name = str(i).replace('-', ' ').replace('(', '').replace(')', '')
    arcpy.FeatureClassToFeatureClass_conversion('points', output, 'points_X_glaciated_{}'.format(name))

