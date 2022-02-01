# 讀取檔案
products = []
with open('Products.csv', 'r') as f:
    for line in f:
        if '商品,價格' in line:
            continue
        name, price = line.strip().split(',')
        products.append([name, price])
print(products)

# 使用者輸入
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
        break
    price = input('商品金額: ')
    print('結束請按q')
    products.append([name, price])
print(products)

# 列出所有購買紀錄
for p in products:
    print(p[0],'的價格為', p[1])

# 寫入檔案
with open('Products.csv', 'w') as f:
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0] + ',' + p[1] + "\n")
