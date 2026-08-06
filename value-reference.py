#VALUE TYPES

# x = 10
# y = 20
# x = y       # y üzerindeki değer x'e kopyalanır.
# y = 30      # y'deki değişiklik x'i etkilemez çünkü bunlar value type olaarak saklanır.
# print(x, y)

#REFERENCE TYPES

a = ["apple" , "pear"]
b = ["apple" , "pear"]

a = b  # b'nin adresini a'ya kopyalamış oluruz. Çğnkü bütün listeler reference type sahiptir.

a[0] = "grape"
print(a,b)

# liste kopyalama
listA = [10,20]
listB = listA       # adres kopyalar.
listB = listA.copy()       # value type gibi kopyalam yaptığımız için değişiklik artık blistesini etkilemez.
listB = list(listA)        # buda kopyalamanın farklı bir yoludur value type gibi.


listB[0] = 30

print(listA, listB)
     