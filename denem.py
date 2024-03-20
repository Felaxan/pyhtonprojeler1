sayi1 = float(input("Lütfen birinci sayıyı giriniz: "))
sayi2 = float(input("Lütfen ikinci sayıyı giriniz: "))

islem = input("Yapmak istediğiniz işlem (+/-///*): ")


if islem=="+":
    toplam = sayi1+sayi2
    print("Toplama sonucunuz: ",toplam)
elif islem=="-":
    toplam = sayi1-sayi2
    print("Çıkartma Sonucunuz: ",toplam)
elif islem=="/":
    toplam = sayi1/sayi2
    print("Bölme Sonucunuz: ",toplam)
elif islem=="*":
    toplam = sayi1*sayi2
    print("Çarpma Sonucunuz: ",toplam)
 