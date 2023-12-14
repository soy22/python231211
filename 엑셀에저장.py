import openpyxl
import random

# 전자제품 데이터 생성
products = []
for i in range(1, 101):
    product_id = f"P{i:03d}"
    product_name = f"제품{i}"
    quantity = random.randint(1, 10)
    price = round(random.uniform(10, 1000), 2)
    products.append((product_id, product_name, quantity, price))

# 엑셀 파일 생성 및 데이터 쓰기
wb = openpyxl.Workbook()
ws = wb.active

# 열 제목 추가
ws.append(["제품ID", "제품명", "수량", "가격"])

# 데이터 추가
for product in products:
    ws.append(product)

# 엑셀 파일 저장
file_path = "c:\\work\\products.xlsx"
wb.save(file_path)

print(f"데이터가 성공적으로 생성되어 {file_path}에 저장되었습니다.")
