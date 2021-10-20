from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")
ws = wb.active

# ws.insert_rows(8) # 8번째 줄이 비워짐
# ws.insert_rows(8,5) # 8번째 줄 위치에 5줄을 추가로 생성

# ws.insert_cols(2) # B번째 열이 비워짐
ws.insert_cols(2, 3) # B번째 열부터 3열 추가로 생성

wb.save("sample_insert_rows.xlsx")