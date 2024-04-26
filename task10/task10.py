import string

import arcpy

arcpy.env.overwriteOutput = True

Data = r"C:\Users\zidan\Desktop\GISProj\Data"
arcpy.env.workspace = Data

output = r"C:\Users\zidan\Desktop\GISProj\Output\task10"

points = r"C:\Users\zidan\Desktop\GISProj\Data\ne_10m_geography_regions_points.shp"

fields = [f.name for f in arcpy.ListFields(points)]

with arcpy.da.UpdateCursor(points, fields) as cursor:
    for row in cursor:
        for column in range(41):
            if(type(row[column]) is unicode):
                cell = row[column].encode('ascii', 'ignore')
                if(cell == " " or len(cell)==0):
                    row[column] = "empty"
                    cursor.updateRow(row)
