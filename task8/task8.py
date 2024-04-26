import arcpy

arcpy.env.overwriteOutput = True

Data = r"C:\Users\zidan\Desktop\GISProj\Data"
arcpy.env.workspace = Data

output = r"C:\Users\zidan\Desktop\GISProj\Output\task8"

rivers_lake = r"C:\Users\zidan\Desktop\GISProj\Data\ne_10m_rivers_lake_centerlines.shp"

arcpy.MakeFeatureLayer_management(rivers_lake, 'rivers_lake', """ "featurecla"='Lake Centerline' """)
arcpy.FeatureClassToFeatureClass_conversion('rivers_lake', output, 'rivers_lake_X_Lake_Centerline')