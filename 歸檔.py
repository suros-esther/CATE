# [整理]指定目錄下的檔名=>Excel
import pandas as pd
import os
import shutil

# input("請輸入檔案資料夾路徑：")
SourcePath = "C:\\Users\\Esther.Chang\\Desktop\\第二個程式\\測試資料夾\\似層"
List = os.listdir(SourcePath)
# print(List)


All = list()

i = 0
for i in range(0, len(os.listdir(SourcePath))):
    divext = list(os.path.splitext(List[i]))  # 分開副檔名
    divdash = divext[0].split('_')  # 依_分開檔名
    divdash.append(divext[1])
    All.append(divdash)
    i += 1


# Export = os.getcwd() + '\\' + 'export.xlsx'
df = pd.DataFrame(All)
df.columns = ["Category", "Name", "Extension"]
# df.to_excel(Export, sheet_name='20220902', index=False)  # 輸出Excel

# [歸類]依類別建立資料夾並移動檔案
# <從All取出>列出類別的List
# j = 0  #
# Cate = list()
# for j in range(0, len(All)):
#     a = All[j][0]
#     if a not in Cate:
#         Cate.append(a)
#     j += 1

# <從df取出>列出類別的List
Cate = list()
for k in range(0, len(df)):
    a = df['Category'].values[k]
    if a not in Cate:
        Cate.append(a)
    k += 1


index = 0
for index in range(0, len(Cate)):
    CreatePath = SourcePath + '\\' + Cate[index]
    if os.path.isdir(CreatePath) == False:
        os.mkdir(CreatePath)  # 建立類別資料夾
    index += 1

# First = list()
i = 0
j = 0
for j in range(0, len(Cate)):
    for i in range(0, len(List)):
        if Cate[j] in List[i]:
            source = SourcePath + "\\" + List[i]
            Name = List[i].removeprefix(Cate[j] + '_')
            destination = SourcePath + "\\" + Cate[j] + "\\" + Name
            shutil.move(source, destination)

        i += 1
    j += 1


# # replace
# i = 0

# for i in range(0, len(List)):
#     symbollist = ['-', ' ']
#     for j in range(0, len(symbollist)):
#         Current = List[i].replace(symbollist[j], '')
#         print(Current)
#     j += 1

# i += 1
# print(List)
# # replace
