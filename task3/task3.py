import arcpy

Data = r"C:\Users\zidan\Desktop\GISProj\Data"
arcpy.env.workspace = Data

arcpy.env.overwriteOutput = True

points = r"C:\Users\zidan\Desktop\GISProj\Data\ne_10m_geography_regions_elevation_points.shp"

cursor = arcpy.UpdateCursor(points, """ "featurecla"='mountain' AND "name"='' """, ['name', 'featurecla', 'comment', 'long_x', 'lat_y'])
for i in cursor:
    print(i.getValue('long_x'), i.getValue('lat_y' ))
    print(i.getValue('comment'))
    i.setValue('name', i.getValue('comment'))
    cursor.updateRow(i)


