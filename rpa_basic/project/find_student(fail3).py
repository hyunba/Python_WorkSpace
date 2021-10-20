import openpyxl
import operator

wb = openpyxl.load_workbook("sample.xlsx") 
ws = wb.active 
wo = openpyxl.Workbook() 

ro = int(input("찾고싶은 열을 입력하세요 :")) 
find = int(input("찾고 싶은 값을 입력하세요 :")) 
for i in ws.rows: # 세로 전체(행)까지 
    for j in range(0,5): 
        if(operator.eq(i[ro].value, find)): 
            print(i[j].value)
