print("Yapmak İstediğiniz İşlemi Seçiniz. ( '1' Toplama - '2' Çıkarma - '3' Çarpma - '4' Bölme ) ")
def Carp(x, y):
   return x * y
 
def Bol(x, y):
   return x / y 
def Topla(x, y):
   return x + y
 
def Cikar(x, y):
   return x - y
secim = input("Seçim :")
 
sayi1 = int(input("1. Sayı Giriniz: "))
sayi2 = int(input("2. Sayı Giriniz: "))
 
if secim == '1':
    
   print("Toplamı: " , sayi1 , " + " , sayi2 , " = " , Topla(sayi1,sayi2) )
 
elif secim == '2':
    
   print("Farkı: " , sayi1 , " - ", sayi2 , " = " , Cikar(sayi1,sayi2) )
 
elif secim == '3':
    
   print("Çarpımı: " , sayi1 , " * ", sayi2 , " = " , Carp(sayi1,sayi2) )
 
elif secim == '4':
    
   print("Bölümü: " , sayi1 , "/ " , sayi2 , " = ", Bol(sayi1,sayi2) )
else:
   print(" Lütfen işlem yapmak için 1-2-3-4 seçeneklerinden birini seçiniz. ")