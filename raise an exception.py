# 2- Girilen parola içinde türkçe karakter hatası veriniz.

def parolaKontrol(parola):
    turkce_karakterler = "ŞşÇçĞğÜüÖöıİ"

    for i in parola:
        if i in turkce_karakterler:
            raise TypeError("Parola türkçe karakter içeremez.")

    print('geçerli parola')

parola = input('parola: ')

try:
    parolaKontrol(parola)
except TypeError as e:
    print(e)