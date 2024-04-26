import arcpy

arcpy.env.overwriteOutput = True

Data = r"C:\Users\zidan\Desktop\GISProj\Data"
arcpy.env.workspace = Data

output = r"C:\Users\zidan\Desktop\GISProj\Output\task7"

region_polys = r"C:\Users\zidan\Desktop\GISProj\Data\ne_10m_geography_regions_polys.shp"

arcpy.MakeFeatureLayer_management(region_polys, 'region_polys')

cusrsor = arcpy.SearchCursor('region_polys', ['NAME', 'REGION', 'WIKIDATAID'])
for i in cusrsor:
    print(i.getValue('NAME') + ',' + i.getValue('REGION') + ',' + i.getValue('WIKIDATAID') )