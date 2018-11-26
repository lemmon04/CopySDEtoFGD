import arcpy, os
from arcpy import env

env.workspace = ""
outputFGD = ""

features = arcpy.ListFeatureClasses()
for feature in features:
    feature_split = feature.split(".")
    schema = feature_split[1]
    name = feature_split[2]
    try:
        arcpy.CopyFeatures_management(feature,outputFGD + "/" + schema + "_" + name)
    except:
        print feature

tables = arcpy.ListTables()
for table in tables:
    table_split = table.split(".")
    schema_table = table_split[1]
    name_table = table_split[2]
    try:
        arcpy.Copy_management(table,outputFGD + "/" + schema_table + "_" + name_table)
    except:
        print table
    
