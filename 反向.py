from ast import Or
import pandas as pd
import os
import shutil

# input("請輸入檔案資料夾路徑：")
SourcePath = "C:\\Users\\Esther.Chang\\Desktop\\第二個程式\\測試資料夾\\似層"
List = os.listdir(SourcePath)

i = 0

for i in range(0, len(List)):
    a = List[i]
    Path = SourcePath + "\\" + a
    NameList = os.listdir(Path)
    for j in range(0, len(NameList)):
        NewNameList = str(a) + "_" + NameList[j]
        OriDoc = Path + "\\" + NameList[j]
        DesDoc = Path + "\\" + NewNameList
        os.renames(OriDoc, DesDoc)
        # move out
        oriPath = DesDoc
        desPath = SourcePath + "\\" + NewNameList
        shutil.move(oriPath, desPath)
    j += 1
    os.rmdir(Path)
i += 1
