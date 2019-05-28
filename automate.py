import os
import ntpath
import xml.etree.ElementTree as ET
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
itemTypes=['ImageItem','BarcodeItem','TextItem']
def Remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list
    
path = 'C:\\Users\\**\\Desktop\\cacheid list\\Corrected Labels'
folders = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for folder in d:
        folders.append(os.path.join(r, folder))
writer = ExcelWriter('listOfCacheIds.xlsx')
for f in folders:
    files = []
    # r=root, d=directories, f = files
    for r, d, fle in os.walk(f):
        for file in fle:
            if '.xml' in file:
                files.append(os.path.join(r, file))
    cacheids=list(str())
    filen=list()
    for fil in files:
        tree = ET.parse(fil)
        root = tree.getroot()
        caid=list(str())
        for it in itemTypes:
            for neighbor in root.iter(it):
                caid.append(neighbor.attrib['CacheItemId'])
                #print(caid)
        caid = [i for i in caid if i]
        caid=Remove(caid)

        for c in caid : 
            cacheids.append(c)
        lof=[ntpath.basename(fil)] * len(caid)
        for l in lof : 
            filen.append(l)
    df=pd.DataFrame({'Cacheid':cacheids,
                'Label':filen})
    df.to_excel(writer,ntpath.basename(f),index=False)
writer.save()
