# task 1

import arcpy

Data = r"..\Data"
output = r"..\Output\Task2"

arcpy.env.workspace = Data

# List of features
LIST = arcpy.ListFeatureClasses()
print(LIST)