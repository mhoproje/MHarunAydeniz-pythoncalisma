# Bir aracın yakıt tipine göre (benzin,dizel,lpg) belirtilen bir mesafede ne kadar yakıt masrafı olduğunu
# hesaplayan uygulamayı yapınız.

benzinFiyat = 17.80
dizelFiyat = 21.34
lpgFiyat = 10.60
toplamYakitUcreti = 0

ortalamaYakitTuketimi = float(input('100 km deki ortalama yakıt tüketimi: '))
gidilecekYol = float(input('gidilecek yol kaç km: '))
yakitTipi = input('yakıt tipiniz nedir: ')

toplamYakitTuketimi = gidilecekYol * (ortalamaYakitTuketimi / 100)

if(yakitTipi == "benzin"):
    toplamYakitUcreti = benzinFiyat * toplamYakitTuketimi
elif (yakitTipi == "dizel"):
    toplamYakitUcreti = dizelFiyat * toplamYakitTuketimi
elif (yakitTipi == "lpg"):
    toplamYakitUcreti = lpgFiyat * toplamYakitTuketimi
else:
    print('yanlış yakıt tipi girdiniz.')

if (toplamYakitUcreti != 0):
    print(toplamYakitUcreti)