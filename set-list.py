fruits = {"apple", "pear", "cherry", "apple"}
fruits2 = {"apple", "pear", "cherry", "melon"}


# result = furits[0] # index ile erişilmez setlere.
# aynı şey iki defa varsa birini ekrana yazar o yüzden temizleme yaparken set kullanmak mantıklıdır.

for x in fruits:
    print(x)

result1 = "apple" in fruits      #apple meyveler içinde var mı bunu sorgularız.
print(result1)

fruits.add("watermelon")        #herhangi bir indexeeklenir program her çalıştığında aynı yerde olması gerekmez.
fruits.update(fruits2)          #ikisinde ortak olanları bir kere yazar onun dışında hepsini yazar yeni listeye.
fruits.remove("apple")          #silme işlemi yapar ama eleman yoksa hata üretir.(raise an error)
fruits.discard("apple")         #silme işlemi yapar eleman yoksa hata üretmez.
fruits.pop()                    #indexleme olmadığı içğin herhangi bir elemanı siler.

result = fruits
print(result)

