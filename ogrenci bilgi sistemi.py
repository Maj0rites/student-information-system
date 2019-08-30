import sqlite3
import time




def ogrenciBilgi(ogrenciAdi):
    bilgi = kalem.execute("SELECT * FROM ogrenciler WHERE ogrenci_ad=?",(ogrenciAdi,))
    a = bilgi.fetchall()
    if(len(a)==0):
        print("Öğrenci bulunamadı :(")
        return 0
    for i in bilgi.fetchall():
        print("Öğrenci numarası:",i[0],"Öğrenci İsmi:",i[1])
        time.sleep(3)

def yeniOgrenci(ogrenciAd):
    kalem.execute("INSERT INTO ogrenciler (ogrenci_ad) VALUES (?)",(ogrenciAd,))
    print(ogrenciAd,"isimli öğrenci başarıyla kaydedilmiştir.")
    time.sleep(3)

def notEkle(ogrenciNo,ders,dersNotu):
    bilgi = kalem.execute("SELECT * FROM ogrenciler WHERE ogrenci_no = ?",(ogrenciNo,))
    a = bilgi.fetchall()

    if(ders=="M"):
        len(a)
        if(len(a)==0):
            kalem.execute("INSERT INTO dersNotlari (ogrenci_no,matematik) VALUES (?,?) ",(ogrenciNo,dersNotu))
        else:
            kalem.execute("UPDATE dersNotlari SET matematik = ? WHERE ogrenci_no = ?",(dersNotu,ogrenciNo))
    if (ders == "F"):
        if(len(a)==0):
            kalem.execute("INSERT INTO dersNotlari (ogrenci_no,fizik) VALUES (?,?) ",(ogrenciNo,dersNotu))
        else:
            kalem.execute("UPDATE dersNotlari SET fizik = ? WHERE ogrenci_no = ?",(dersNotu,ogrenciNo))
    if (ders == "K"):
        if(len(a)==0):
            kalem.execute("INSERT INTO dersNotlari (ogrenci_no,kimya) VALUES (?,?) ",(ogrenciNo,dersNotu))
        else:
            kalem.execute("UPDATE dersNotlari SET kimya = ? WHERE ogrenci_no = ?",(dersNotu,ogrenciNo))
    if (ders == "B"):
        if(len(a)==0):
            kalem.execute("INSERT INTO dersNotlari (ogrenci_no,biyoloji) VALUES (?,?) ",(ogrenciNo,dersNotu))
        else:
            kalem.execute("UPDATE dersNotlari SET biyoloji = ? WHERE ogrenci_no = ?",(dersNotu,ogrenciNo))
    time.sleep(3)

def devamsizlikEkle(ogrenciNo,tarih):
    kalem.execute("INSERT INTO devamsizlik VALUES (?,?)",(ogrenciNo,tarih))
    print("Devamsızlık başarıyla eklenmiştir.")
    time.sleep(3)

def dersNotu(ogrenciAd):
    numara = kalem.execute("SELECT ogrenci_no FROM ogrenciler WHERE ogrenci_ad = ?",(ogrenciAd,))
    numara = numara.fetchone()[0]
    notlar = kalem.execute("SELECT * FROM dersNotlari WHERE ogrenci_no = ?",(numara,))
    a = notlar.fetchall()
    print("Matematik:",a[0][1],"Fizik:",a[0][2],"Kimya:",a[0][3],"Biyoloji:",a[0][4])
    time.sleep(3)

def devamsizlikOgren(ogrenciAd):
    numara = kalem.execute("SELECT ogrenci_no FROM ogrenciler WHERE ogrenci_ad = ?",(ogrenciAd,))
    numara = numara.fetchone()[0]
    devamsizlik = kalem.execute("SELECT * FROM devamsizlik WHERE ogrenci_no = ?",(numara,))
    a = devamsizlik.fetchall()
    for i in a:
        print("Gelmediği tarih",i[1])
    time.sleep(3)



print("Hoşgeldiniz.")
while True:
    baglanti = sqlite3.connect("ogrenciBilgi.db")
    kalem = baglanti.cursor()

    print("Öğrenci bilgilerini görmek için ->1 \nYeni öğrenci eklemek için -> 2\nDers notu eklemek için -> 3\nDevamsızlık eklemek için -> 4")
    secim = input()

    if(secim=="1"):
        isim = input("Öğrencinin adını giriniz: ")
        a = ogrenciBilgi(isim)
        if(a != 0):
            komut = input("Ders notlarını öğrenmek için -> 1 || Devamsızlıklarını öğrenmek için -> 2 ")
            if (komut=="1"):
                dersNotu(isim)
            elif(komut=="2"):
                devamsizlikOgren(isim)

    elif(secim=="2"):
        isim = input("Eklemek istediğiniz öğrencinin adını giriniz: ")
        yeniOgrenci(isim)
    elif(secim=="3"):
        numara = input("Ders notu girmek istediğiniz öğrencinin numarasını giriniz: ")
        print("Matematik için -> M\nFizik için -> F\nKimya için -> K\nBiyoloji için -> B")
        secim = input()
        dersNotu = input("Bu ders için ders notunu giriniz: ")
        notEkle(numara,secim,dersNotu)
    elif(secim=="4"):
        numara = input("Devamsızlığını girmek istediğiniz öğrencinin numarasını giriniz: ")
        tarih = input("Deavmsızlık yaptığı tarihi giriniz: ")
        devamsizlikEkle(numara,tarih)
    baglanti.commit()
    baglanti.close()


