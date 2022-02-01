products = []
while True:
    name = input("請輸入商品名稱: ")
    if name == 'q':
        break
    price = input('商品金額: ')
    products.append([name, price])
print(products)