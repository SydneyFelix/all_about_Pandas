import pandas as pd

#Given an excel file, it modifies it and then creates a number of excel files. You can create the new excel file using the item as file name. You can rename 
#the new sheet as the item. The file is created in a new file path/folder ( ie. output)

data_fields = pd.read_excel("C:\\Users\\PC\\py4e\\Lookup File.xlsx")

unique_values = data_fields['REGION'].unique()
print(unique_values)
print('======================')
print(data_fields.head())
output_path = "C:/Users/PC/py4e/output/"

for item in unique_values:
    newDF = data_fields[data_fields['REGION']==item]
    print(newDF)
    newDF.to_clipboard
    newDF.to_excel("C:/Users/PC/py4e/output/" + item + '.xlsx', sheet_name=item, index=None) 
    
