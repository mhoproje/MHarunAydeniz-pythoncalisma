"""
    Bir aracın km cinsinden gittiği yol bilgisini mil olarak yazdırınız.
    mil = km / 1.609344
"""
print("kaç km yol gittiniz?")
mesafeKm = input()
mesafeMil = float(mesafeKm) / 1.609344
mesafeMil = round(mesafeMil, 2)

print(str(mesafeKm) + " km = " + str(mesafeMil) + " mil.")