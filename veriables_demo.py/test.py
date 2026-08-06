x=int(input("Enter vize notu"))
y=int(input("Enteer final notu"))
gecme_notu=((x*40/100)+(y*60/100))
if gecme_notu >= 60: 
    print("Geçtiniz")
else:
    print("Bu dersi tekrar almanız gerekmektedir")