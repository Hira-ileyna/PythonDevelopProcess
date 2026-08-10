# list = [1,2,3,4]  #elimizde bir liste varken o listeyi for döngüsü ile dolaşabiliriz.

# for i in list:
#     print(i)


# Ama eğer bir liste yok ve biz oluşturmak istiyorsak range methoduu kullanabiliriz.
for i in range(1,100,2):
    print(i)

# rng = range(10)
# result = list(rng)
# print(result)

rng = range(0, -20, -2)
result = list(rng)
print(result)