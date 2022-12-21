# 1- 3 ürün bilgisini (id,ad,fiyat) dictionary içinde saklayınız.
# 2- Ürün id bilgisini kullanıcıdan alıp ilgili ürün bilgisini gösterin.


urunler = {
            '1': {'ad': 'IPhone 11', 'fiyat': '15000'},
            '2': {'ad': 'IPhone 13', 'fiyat': '26000'},
            '3': {'ad': 'IPhone 14', 'fiyat': '30000'}
        }

id = input('aramak istediğiniz ürün id: ')
urun = urunler[id]

print(f'id: {id} ürün adı: {urun["ad"]} ürün fiyatı: {urun["fiyat"]}')


