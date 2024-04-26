import arcpy

arcpy.env.overwriteOutput = True

Data = r"C:\Users\zidan\Desktop\GISProj\Data"
arcpy.env.workspace = Data

output = r"C:\Users\zidan\Desktop\GISProj\Output\task6"

rivers_lake = r"C:\Users\zidan\Desktop\GISProj\Data\ne_10m_rivers_lake_centerlines.shp"

for i in range(13):
    arcpy.MakeFeatureLayer_management(rivers_lake, 'rivers_lake', """ "scalerank"={} """.format(i))
    arcpy.FeatureClassToFeatureClass_conversion('rivers_lake', output, 'rivers_lake_with_scalerank_{}'.format(i))
