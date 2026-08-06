website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

# 1- 'course' karakter diziminde kaç karakter bulunmaktadır ?

result = len(course)
lenght = len(website)

# 2- 'website' içinden www karakterlerini alın.

result = website[7:10]

# 3- 'website' içinden com karakterlerini alın.
result = website[22:25]
result = website[lenght-3:lenght]


# 4- 'course' içinden ilk 15 ve son 15 karakteri alın.

result = course[:15]
result = course[0:15]
result = course[-15:]
# 5- 'course' ifadesindeki karakterleri tersten yazdırın.

result = course[::-1]
s = '12345' *5
print(s[::5])

name, surname, age, job = 'Bora','Yılmaz', 32, 'mühendis'
# 6-Yukarda verilen değişkenlere ekrana aşağıdaki ifadeyi yazdırın.
# 'Benim adım Bora Yılmaz, Yaşım 32 ve mesleğim mühendis.'

result = "Benim adım "+ name+ " " + surname+ ", Yaşım "+ str(age)+ " ve mesleğim "+ job+ " ."
result = 'Benim adım {0} {1}, Yaşım {2} ve mesleğim {3}.'.format(name,surname,age,job)
result = 'Benim adım {} {}, Yaşım {} ve mesleğim {}.'.format(name,surname,age,job)
result = f"Benim adım {name} {surname}, Yaşım {age} ve mesleğim {job}."
result = f'"Benim adım" {name} {surname}, Yaşım {age} ve mesleğim {job}.'

# 7-'Hello world' ifadesindeki w harfini 'W' ile değiştirin.

s = 'Hello world'
s = s[0:6] + 'W'+ s[-4:]
print(s)

# 8- 'abc' ifadesini yan yana 3 defa yazdırın.

result = 'abc ' * 3
print(result)