import arcpy

arcpy.env.overwriteOutput = True

Data = r"C:\Users\zidan\Desktop\GISProj\Data"
arcpy.env.workspace = Data

output = r"C:\Users\zidan\Desktop\GISProj\Output\task5"

region_points = r"C:\Users\zidan\Desktop\GISProj\Data\ne_10m_geography_regions_points.shp"

sub_regions = ['Indian Ocean', 'North Pacific Ocean', 'South Pacific Ocean']

for i in sub_regions:
    print('---------------------------------------------')
    print(i + ':')
    print('----------------')
    arcpy.MakeFeatureLayer_management(region_points,  'points', """ "subregion"='{}' """.format(i))
    arcpy.FeatureClassToFeatureClass_conversion('points', output, 'regions_X_{}'.format(i))
    cursor = arcpy.SearchCursor('points', ['name'])
    for x in cursor:
        print(x.getValue('name'))
