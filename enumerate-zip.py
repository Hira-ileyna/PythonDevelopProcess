# brands = ["opel","bmw","togg"]
# index = 1
# for brand in brands:
#     print(f"{index}-{brand}")
#     index += 1

# obj1 = enumerate(brands,1)

# print(type(obj1))
# print(list(obj1))

# for brand in enumerate(brands):
#     print(brand)

# for index, brand in enumerate(brands,1):
#     print(f"{index}-{brand}")


#zip: birden fazla liste varsa birleştirmeye yarayan methottur.

number = [100,200,300]
student = ["Ali", "Ayse", "Canan","Mehmet"] #Mehtmet ile eşleşen bir kayıt olmadığını için  Mehmet göz ardı edilir ve çıktıya yansımaz.

print(list(zip(number, student)))

for no, name in zip(number,student):
    print(no, name)
