products = [
    {"productName" : "Hp Victus", "price" : 32999},
    {"productName" : "Lenova ThinkPad", "price" : 25499},
    {"productName" : "Apple Mackbook", "price" : 49999},
    {"productName" : "Huawei Matebook", "price" : 26999},
    {"productName" : "Casper Nirvana", "price" : 20000},
    ]
for i in products:
    print(f"{i["productName"]} marka ürünün fiyatı {i["price"]}")

sum = 0
for i in products:
    sum += i["price"]
print(sum)

for i in products:
    if 25000 < i["price"] < 40000:
        print(i["productName"])

word = input("Aramak istediğiniz ürün: ")

for i in products:
    if(i["productName"].lower().find(word.lower()) > -1):
        print(i["productName"])