# Bankamatik Uygulaması

HarunHesap = {
    'ad': 'Harun Aydeniz',
    'hesapNo': '13245678',
    'bakiye': 15000,
    'ekHesap': 5000
}

ElifHesap = {
    'ad': 'Elif Biter',
    'hesapNo': '12345678',
    'bakiye': 10000,
    'ekHesap': 3000
}


def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    if hesap['bakiye'] >= miktar:
        hesap['bakiye'] -= miktar
        print('paranızı alabilirsiniz.')
        bakiyeSorgula(hesap)
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']

        if toplam >= miktar:
            ekHesapKullanimi = input('ek hesap kullanılsın mı (e/h)')

            if ekHesapKullanimi == 'e':
                ekhesapKullanilacakMiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= ekhesapKullanilacakMiktar
                print('paranızı alabilirsiniz.')
                bakiyeSorgula(hesap)
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bulunmaktadır.")
        else:
            print('üzgünüz bakiye yetersiz')
            bakiyeSorgula(hesap)


def bakiyeSorgula(hesap):
    print(
        f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesap limitiniz ise {hesap['ekHesap']} TL bulunmaktadır.")


paraCek(HarunHesap, 2000)

print('*****************')

paraCek(HarunHesap, 1000)

paraCek(ElifHesap, 10000)
paraCek(ElifHesap, 1000)
