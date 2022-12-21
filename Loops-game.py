"""
    1-10 arasında rastgele üretilecek bir sayıyı aşağı yukarı
    ifadeleri ile buldurdmaya çalışın.
    "Random modülü kullanın"
    kullanıcıdan kaç hak istediği bilgisini alarak 100 üzerinden
    puanlama yapın.(örn: 10 hak istenilirse her yyanlış tahmin için 10 puan azaltın)
"""
import random

sayi = random.randint(1, 10)
can = int(input('kaç hak kullanmak istersiniz:'))
hak = can
sayac = 0

while hak > 0:
    hak -= 1
    sayac += 1
    tahmin = int(input('tahmin:'))

    if sayi == tahmin:
        print(f'Tebrikler {sayac}. tahminde bildiniz. Toplam puanınız:{100 - (100/can) * (sayac-1) }')
        break
    elif sayi > tahmin:
        print('yukarı')
    else:
        print('aşağı')

    if hak == 0:
        print(f'hakkınız bitti. Tutulan sayı : {sayi}')
